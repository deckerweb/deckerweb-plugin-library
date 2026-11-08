<?php
/** Isolated executable regression checks. No real WordPress database or HTTP requests.
 * Copyright 2026 David Decker – DECKERWEB. SPDX-License-Identifier: GPL-2.0-or-later
 */
error_reporting( E_ALL );
set_error_handler( static function( $severity, $message, $file, $line ) { throw new RuntimeException( "$message at $file:$line" ); } );
define( 'ABSPATH', __DIR__ . '/fixtures/' );
define( 'WP_PLUGIN_DIR', __DIR__ . '/fixtures/plugins' );
$GLOBALS['network'] = 0; $GLOBALS['options'] = []; $GLOBALS['plugins'] = []; $GLOBALS['github'] = ''; $GLOBALS['http_calls'] = 0;
$GLOBALS['wp_version'] = '6.4'; $GLOBALS['cache_clears'] = 0;
class WP_Error {
 public $code; public $message; public $data;
 public function __construct( $code = '', $message = '', $data = null ) { $this->code=$code; $this->message=$message; $this->data=$data; }
 public function get_error_code() { return $this->code; }
 public function get_error_message() { return $this->message; }
 public function get_error_data() { return $this->data; }
}
function is_wp_error( $value ) { return $value instanceof WP_Error; }
function get_site_option( $key, $default = false ) { return $GLOBALS['options'][$GLOBALS['network']][$key] ?? $default; }
function update_site_option( $key, $value ) { $GLOBALS['options'][$GLOBALS['network']][$key] = $value; return true; }
function update_option( $key, $value, $autoload = null ) { return update_site_option( $key, $value ); }
function delete_site_option( $key ) { unset( $GLOBALS['options'][$GLOBALS['network']][$key] ); return true; }
function get_plugins() { return $GLOBALS['plugins']; }
function wp_clean_plugins_cache( $updates = true ) { ++$GLOBALS['cache_clears']; }
function get_file_data( $file, $fields ) { return array_map( static function( $field ) { return $field === 'GitHub Plugin URI' ? $GLOBALS['github'] : ''; }, $fields ); }
function determine_locale() { return 'en_US'; }
function wp_parse_url( $url ) { return parse_url( $url ); }
function is_multisite() { return $GLOBALS['network'] > 0; }
function is_network_admin() { return is_multisite(); }
function is_plugin_active_for_network( $file ) { return false; }
function is_plugin_active( $file ) { return false; }
function wp_tempnam( $name ) { return false; }
function wp_safe_remote_get( $url, $args ) { ++$GLOBALS['http_calls']; throw new RuntimeException( 'Unexpected real transport boundary' ); }
function wp_remote_retrieve_response_code( $response ) { return $response['response']['code'] ?? 0; }
function get_site_transient( $key ) { return $GLOBALS['transients'][$key] ?? false; }
$source = getenv( 'LIBRARY_TEST_SOURCE' ) ?: dirname( __DIR__ ) . '/lib';
foreach ( [ 'I18n', 'Catalog', 'Requirements', 'Package', 'NativeUpdates', 'Experience', 'Library' ] as $class ) { require $source . '/src/' . $class . '.php'; }
use Deckerweb\PluginLibrary\V1_3_0\Library;
use Deckerweb\PluginLibrary\V1_3_0\Catalog;
use Deckerweb\PluginLibrary\V1_3_0\Requirements;
use Deckerweb\PluginLibrary\V1_3_0\Package;
use Deckerweb\PluginLibrary\V1_3_0\NativeUpdates;
use Deckerweb\PluginLibrary\V1_3_0\Experience;
$checks = 0; $failures = [];
function verify( $condition, $name ) { ++$GLOBALS['checks']; if ( ! $condition ) { $GLOBALS['failures'][] = $name; fwrite( STDERR, "FAIL $name\n" ); } }
$entries = Catalog::validate( json_decode( file_get_contents( $source . '/catalog.json' ), true ) );
verify( is_array( $entries ), 'real bundled catalog validates' );
$entry = $entries['brand-admin-schemes']; $file = $entry['plugin_file'];
$lib = (new ReflectionClass( Library::class ))->newInstanceWithoutConstructor();
$property = new ReflectionProperty( Library::class, 'catalog' ); $property->setAccessible( true ); $property->setValue( $lib, new Catalog( $source ) );
foreach ( [ 0, 1, 2 ] as $network ) {
 $GLOBALS['network']=$network;
 $good=['Name'=>$entry['name'],'PluginURI'=>'https://github.com/'.$entry['repository'],'UpdateURI'=>'https://github.com/'.$entry['repository'],'Version'=>'1.0.0','RequiresWP'=>'6.4','RequiresPHP'=>'8.0'];
 $GLOBALS['plugins']=[$file=>$good];
 $offer=(object)['plugin'=>$file,'new_version'=>'2.0.0','package'=>'https://github.com/'.$entry['repository'].'/releases/download/v2.0.0/plugin.zip'];
 foreach([false,true] as $online){
  update_site_option(Library::OPTION,['online'=>$online]);
  foreach(['0.1.0','1.0.0','2.0.0','99.0.0'] as $catalog_version){
   $metadata=array_replace($entry,['version'=>$catalog_version,'requires_wp'=>'99.0','requires_php'=>'99.0']);
   $state=(object)['response'=>[$file=>$offer],'checked'=>[$file=>'0.0.1']];$GLOBALS['transients']['update_plugins']=$state;
   verify(NativeUpdates::offer($metadata,$GLOBALS['plugins'],$state)->new_version==='2.0.0','ordinary offer independent of catalog version/settings');
   verify(Experience::matches('updates',$metadata,$GLOBALS['plugins'],$state),'status filter uses normal offer');
   verify($lib->updater_release('https://github.com/'.$entry['repository'],$file,true)===false,'legacy shim always selects direct updates');
   verify(is_wp_error($lib->updater_package('https://github.com/'.$entry['repository'],$file,$entry['download_url'])),'old package provider cannot create catalog update archive');
   verify($lib->update_download(false,$offer->package,new stdClass(),['plugin'=>$file])===false,'retired download hook leaves normal updater alone');
  }
 }
 foreach(['missing'=>null,'string'=>'bad','same'=>(object)['plugin'=>$file,'new_version'=>'1.0.0','package'=>$offer->package],'downgrade'=>(object)['plugin'=>$file,'new_version'=>'0.9.0','package'=>$offer->package],'wrong-file'=>(object)['plugin'=>'foreign/foreign.php','new_version'=>'2.0.0','package'=>$offer->package],'http'=>(object)['plugin'=>$file,'new_version'=>'2.0.0','package'=>'http://example.org/plugin.zip'],'credentials'=>(object)['plugin'=>$file,'new_version'=>'2.0.0','package'=>'https://user:secret@example.org/plugin.zip'],'newline'=>(object)['plugin'=>$file,'new_version'=>'2.0.0','package'=>$offer->package."\n"],'legacy'=>(object)['plugin'=>$file,'new_version'=>'2.0.0','package'=>$offer->package,'dwl_managed'=>true]] as $case=>$bad){
  verify(NativeUpdates::offer($entry,$GLOBALS['plugins'],(object)['response'=>[$file=>$bad]])===null,'invalid/stale native offer rejected '.$case);
 }
 verify(NativeUpdates::offer($entry,[],(object)['response'=>[$file=>$offer]])===null,'missing plugin never has update action');
 verify(NativeUpdates::offer($entry,[$file=>array_replace($good,['Version'=>'3.0.0'])],(object)['response'=>[$file=>$offer]])===null,'manually newer installation never downgraded');
 verify(NativeUpdates::offer($entry,[$file=>array_replace($good,['Version'=>'2.0.0'])],(object)['response'=>[$file=>$offer]])===null,'same version is not an update');
 verify(count(NativeUpdates::issues((object)['requires'=>'99.0','requires_php'=>'99.0']))===2,'actual offered platform minimums enforced');
 verify(NativeUpdates::issues($offer)===[],'catalog minimums do not become update requirements');
 $old=(object)['new_version'=>'0.5.0','dwl_managed'=>true];$state=(object)['response'=>[$file=>$old,'foreign/foreign.php'=>$offer]];$pruned=$lib->updates($state);
 verify(!isset($pruned->response[$file])&&$pruned->response['foreign/foreign.php']===$offer,'retired managed offer removed, normal provider preserved');
 verify(isset($state->response[$file]),'stored state not mutated during read');
 verify($lib->updates((object)['response'=>[$file=>$offer]])->response[$file]===$offer,'no ordinary offer rewritten');
 verify(NativeUpdates::offer($entry,$GLOBALS['plugins'],false)===null,'missing update cache is not a GitHub check');
 $future = array_replace($entry,['requires_wp'=>'99.0','requires_php'=>'99.0','dependencies'=>[]]);
 verify(Requirements::check($future,[$file=>$good],false,true)===[],"installed requirements network $network");
 verify(count(Requirements::check($future,[$file=>$good],false,false))===2,"offered requirements network $network");
 verify(count(Requirements::check($future,[],false,true))===2,"uninstalled target uses offered minimums network $network");
 verify(count(Requirements::check($entry,[$file=>array_replace($good,['RequiresPHP'=>'99.0'])],false,true))===1, 'installed incompatible PHP still rejected');
 verify(count(Requirements::check($entry,[$file=>array_replace($good,['RequiresWP'=>'99.0'])],false,true))===1, 'installed incompatible WP still rejected');
 verify(Requirements::check($future,[$file=>array_replace($good,['RequiresPHP'=>'','RequiresWP'=>''])],false,true)===[], 'empty installed minimums do not inherit future requirements');
 $versioned = array_replace($entry,['network_activation'=>false,'network_activation_min_version'=>'2.0.0','dependencies'=>[['name'=>'Parent','plugin_file'=>'parent/parent.php','min_version'=>'1.0.0']],'dependency_rules'=>[['plugin_file'=>'parent/parent.php','since_version'=>'2.0.0','mode'=>'pause']],'version'=>'2.0.0']);
 verify(!Requirements::dependencies_for($versioned,[$file=>$good],true)[0]['_advisory'],'older target retains required dependency');
 verify(Requirements::dependencies_for($versioned,[$file=>$good],false)[0]['_advisory'],'offered target uses versioned pause');
 verify(count(Requirements::check($versioned,[$file=>$good],true,true))===2,'old network and dependency restrictions retained');
 $target_issues = Requirements::check($versioned,[$file=>$good],true,false);
 verify(version_compare(PHP_VERSION,$versioned['requires_php'],'>=') ? $target_issues===[] : count($target_issues)===1,'new network and pause target respects offered PHP minimum');
}
verify($GLOBALS['http_calls']===0,'installed update selection and legacy adapters issue no HTTP');
// Independent keys make write order irrelevant for distinct records. API doubles
// intentionally do not claim a concurrent MySQL or persistent-cache integration test.
if (method_exists(Library::class,'remember_managed')) {
 $remember=new ReflectionMethod(Library::class,'remember_managed');$remember->setAccessible(true);
 $lookup=new ReflectionMethod(Library::class,'managed_repository');$lookup->setAccessible(true);
 foreach([0,1,2] as $network){$GLOBALS['network']=$network;
  foreach(['a','b','c'] as $id){$remember->invoke(null,['plugin_file'=>"$id/$id.php",'repository'=>"deckerweb/$id"]);}
  foreach(['a','b','c'] as $id){verify($lookup->invoke(null,"$id/$id.php")==="deckerweb/$id","independent managed record $id network $network");}
 }
 $GLOBALS['network']=3;verify($lookup->invoke(null,'a/a.php')==='','network management isolation');
} else { verify(false,'independent management records implemented'); }
$track=new ReflectionMethod(Package::class,'track');$track->setAccessible(true);
$untrack=new ReflectionMethod(Package::class,'untrack');$untrack->setAccessible(true);
foreach([0,1,2] as $network){$GLOBALS['network']=$network;
 $a='/tmp/dwl-a.zip';$b='/tmp/dwl-b.zip';$track->invoke(null,$a);$track->invoke(null,$b);$untrack->invoke(null,$a);
 verify(get_site_option('deckerweb_library_temp_v3_'.hash('sha256',$b))===$b,"untrack A preserves B network $network");
 verify(get_site_option('deckerweb_library_temp_v3_'.hash('sha256',$a),null)===null,"untrack A removes own key network $network");
}
foreach([new WP_Error('http','cURL error 28: secret=/private/path'),['response'=>['code'=>503]]] as $error){$result=Catalog::request_error($error,'package');verify(strpos($result->get_error_message(),'secret')===false && strpos($result->get_error_message(),'/private')===false,'transport diagnostics redact raw details');}
fwrite(STDOUT,json_encode(['php'=>PHP_VERSION,'checks'=>$checks,'failures'=>$failures,'http_calls'=>$GLOBALS['http_calls']],JSON_PRETTY_PRINT)."\n");
exit($failures ? 1 : 0);

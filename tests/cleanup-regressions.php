<?php
/** Final-host cleanup with explicit WordPress storage doubles; no site is loaded.
 * Copyright 2026 David Decker – DECKERWEB. SPDX-License-Identifier: GPL-2.0-or-later
 */
error_reporting(E_ALL);
set_error_handler(static function($severity,$message,$file,$line){throw new RuntimeException("$message at $file:$line");});
define('ABSPATH',__DIR__.'/fixtures/');define('WP_UNINSTALL_PLUGIN','host/host.php');
$GLOBALS['options']=[];$GLOBALS['other_host']=false;$GLOBALS['deleted_users']=[];$GLOBALS['multisite']=true;
$temporary=sys_get_temp_dir().'/dwl-regression-'.bin2hex(random_bytes(6));mkdir($temporary,0700);define('WP_PLUGIN_DIR',$temporary.'/plugins');
register_shutdown_function(static function()use($temporary){foreach(glob($temporary.'/*')?:[]as$file){if(is_file($file))unlink($file);}rmdir($temporary);});
function is_multisite(){return $GLOBALS['multisite'];}
function plugin_basename($file){return substr($file,strlen(WP_PLUGIN_DIR)+1);}
function wp_clean_plugins_cache($unused=false){}
function get_plugins(){return $GLOBALS['other_host']?['other/other.php'=>[]]:[];}
function get_current_blog_id(){return 1;}
function get_main_site_id($network){return 1;}
function get_main_network_id(){return 1;}
function get_networks($args){return[1,2];}
function get_network_option($network,$key,$default=false){return $GLOBALS['options'][$network][$key]??$default;}
function delete_network_option($network,$key){unset($GLOBALS['options'][$network][$key]);}
function get_option($key,$default=false){return get_network_option(0,$key,$default);}
function delete_option($key){delete_network_option(0,$key);}
function wp_cache_delete($key,$group){}
function delete_metadata($type,$id,$key,$value,$all){$GLOBALS['deleted_users'][]=$key;}
function get_temp_dir(){return $GLOBALS['temporary'].'/';}
function wp_delete_file($file){unlink($file);}
class RegressionDB {
 public $options='options';public $sitemeta='sitemeta';
 public function esc_like($value){return addcslashes($value,'_%\\');}
 public function prepare($query,...$args){return[$query,$args];}
 public function get_col($statement){[$query,$args]=$statement;$network=0;if(strpos($query,'site_id = %d')!==false){$network=array_shift($args);}$result=[];
  foreach(array_keys($GLOBALS['options'][$network]??[])as$key){foreach($args as$pattern){$prefix=str_replace(['\\_','\\%','\\\\'],['_','%','\\'],rtrim($pattern,'%'));if(strpos($key,$prefix)===0){$result[]=$key;break;}}}return$result;
 }
}
$wpdb=new RegressionDB();
if (in_array('--older-alias',$argv,true)) { function deckerweb_library_uninstall_v3(string $file): bool { return false; } }
require dirname(__DIR__).'/lib/lifecycle.php';
$checks=0;
function verify($condition,$name){++$GLOBALS['checks'];if(!$condition){throw new RuntimeException($name);}}
foreach([true,false]as$multisite){$GLOBALS['multisite']=$multisite;$networks=$multisite?[1,2]:[0];$GLOBALS['options']=[];
 foreach($networks as$network){$delete=$network!==2;$GLOBALS['options'][$network]['deckerweb_library_settings_v1']=['delete_settings'=>$delete];
  $own=$temporary.'/dwl-package-'.$network.'.zip';file_put_contents($own,'owned');
  $foreign=$temporary.'/foreign-'.$network.'.txt';file_put_contents($foreign,'preserve');
  $GLOBALS['options'][$network]['deckerweb_library_temp_v3_'.hash('sha256',$own)]=$own;
  $GLOBALS['options'][$network]['deckerweb_library_temp_v3_'.hash('sha256',$foreign)]=$foreign;
  $GLOBALS['options'][$network]['deckerweb_library_managed_v2_'.hash('sha256','a/a.php')]='deckerweb/a';
  $GLOBALS['options'][$network]['foreign_option']='retain';
 }
 // An installed inactive host must protect both old and new storage. A real
 // marker fixture is used rather than trusting active-plugin state.
 $other=WP_PLUGIN_DIR.'/other/includes/deckerweb-plugin-library';mkdir($other,0700,true);file_put_contents($other.'/bootstrap.php','<?php');$GLOBALS['other_host']=true;
 verify(deckerweb_library_uninstall_v4(WP_PLUGIN_DIR.'/host/host.php')===false,'remaining host prevents cleanup');
 foreach($networks as$network){verify(file_exists($temporary.'/dwl-package-'.$network.'.zip'),'remaining host preserves temp data');}
 unlink($other.'/bootstrap.php');rmdir($other);rmdir(dirname($other));rmdir(dirname($other,2));rmdir(WP_PLUGIN_DIR);$GLOBALS['other_host']=false;
 verify(deckerweb_library_uninstall_v4(WP_PLUGIN_DIR.'/host/host.php')===true,'final host cleanup completes');
 foreach($networks as$network){verify(!file_exists($temporary.'/dwl-package-'.$network.'.zip'),'owned crash artifact removed');verify(file_exists($temporary.'/foreign-'.$network.'.txt'),'foreign file preserved');
  verify(!isset($GLOBALS['options'][$network]['deckerweb_library_temp_v3_'.hash('sha256',$temporary.'/dwl-package-'.$network.'.zip')]),'temp key removed');
  verify(isset($GLOBALS['options'][$network]['deckerweb_library_managed_v2_'.hash('sha256','a/a.php')])===($network===2),'managed key follows network deletion preference');verify($GLOBALS['options'][$network]['foreign_option']==='retain','foreign option preserved');
 }
}
echo json_encode(['checks'=>$checks,'failures'=>[],'storage'=>'WordPress API doubles; no live database'],JSON_PRETTY_PRINT)."\n";

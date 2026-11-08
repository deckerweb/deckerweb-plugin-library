<?php
/** Exercise actual register methods in concurrent CLI processes with isolated file storage.
 * This is not a WordPress/MySQL or persistent-object-cache integration test.
 * Copyright 2026 David Decker – DECKERWEB. SPDX-License-Identifier: GPL-2.0-or-later
 */
define('ABSPATH',__DIR__.'/fixtures/');
function is_multisite(){return true;}
function get_site_option($key,$default=false){$file=$GLOBALS['store'].'/'.$GLOBALS['scope'].'-'.$key.'.json';return is_file($file)?json_decode(file_get_contents($file),true):$default;}
function update_site_option($key,$value){return file_put_contents($GLOBALS['store'].'/'.$GLOBALS['scope'].'-'.$key.'.json',json_encode($value),LOCK_EX)!==false;}
function delete_site_option($key){$file=$GLOBALS['store'].'/'.$GLOBALS['scope'].'-'.$key.'.json';if(is_file($file))unlink($file);return true;}
require dirname(__DIR__).'/lib/src/Library.php';require dirname(__DIR__).'/lib/src/Package.php';
$managed=new ReflectionMethod('Deckerweb\\PluginLibrary\\V1_3_0\\Library','remember_managed');$managed->setAccessible(true);
$track=new ReflectionMethod('Deckerweb\\PluginLibrary\\V1_3_0\\Package','track');$track->setAccessible(true);
$untrack=new ReflectionMethod('Deckerweb\\PluginLibrary\\V1_3_0\\Package','untrack');$untrack->setAccessible(true);
if(($argv[1]??'')==='worker'){$GLOBALS['store']=$argv[2];$id=(int)$argv[3];$GLOBALS['scope']=$id%2+1;
 for($i=0;$i<40;++$i){$slug="fixture-$id-$i";$managed->invoke(null,['plugin_file'=>"$slug/$slug.php",'repository'=>"deckerweb/$slug"]);usleep(100);}
 $track->invoke(null,"/tmp/dwl-worker-$id-a.zip");$track->invoke(null,"/tmp/dwl-worker-$id-b.zip");$untrack->invoke(null,"/tmp/dwl-worker-$id-a.zip");exit(0);
}
$store=sys_get_temp_dir().'/dwl-parallel-'.bin2hex(random_bytes(6));mkdir($store,0700);$workers=[];
try{
 for($id=0;$id<12;++$id){$pipes=[];$process=proc_open([PHP_BINARY,__FILE__,'worker',$store,(string)$id],[0=>['pipe','r'],1=>['pipe','w'],2=>['pipe','w']],$pipes);if(!is_resource($process))throw new RuntimeException('Cannot launch worker');fclose($pipes[0]);$workers[]=[$process,$pipes];}
 foreach($workers as[$process,$pipes]){$output=stream_get_contents($pipes[1]);$error=stream_get_contents($pipes[2]);fclose($pipes[1]);fclose($pipes[2]);if(proc_close($process)!==0)throw new RuntimeException($output.$error);}
 $checks=0;
 for($id=0;$id<12;++$id){$GLOBALS['store']=$store;$GLOBALS['scope']=$id%2+1;
  for($i=0;$i<40;++$i){$slug="fixture-$id-$i";++$checks;if(get_site_option('deckerweb_library_managed_v2_'.hash('sha256',"$slug/$slug.php"))!=="deckerweb/$slug")throw new RuntimeException('Lost management entry');}
  ++$checks;if(get_site_option('deckerweb_library_temp_v3_'.hash('sha256',"/tmp/dwl-worker-$id-b.zip"))!=="/tmp/dwl-worker-$id-b.zip")throw new RuntimeException('Lost temporary entry');
  ++$checks;if(get_site_option('deckerweb_library_temp_v3_'.hash('sha256',"/tmp/dwl-worker-$id-a.zip"))!==false)throw new RuntimeException('Removed temporary entry resurrected');
 }
 echo json_encode(['workers'=>12,'checks'=>$checks,'failures'=>[],'storage'=>'isolated file-backed WordPress API doubles'],JSON_PRETTY_PRINT)."\n";
}finally{foreach(glob($store.'/*')?:[]as$file){unlink($file);}rmdir($store);}

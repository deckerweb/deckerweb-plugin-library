<?php
/** Public helper contract without a WordPress site or persistent state.
 * Copyright 2026 David Decker – DECKERWEB. SPDX-License-Identifier: GPL-2.0-or-later
 */
define('ABSPATH',__DIR__.'/fixtures/');
function add_action(...$args){}
function plugin_basename($path){return 'fixture/fixture.php';}
require dirname(__DIR__).'/lib/bootstrap.php';
$options=deckerweb_library_updater_options_v1('/fixture/fixture.php','https://github.com/deckerweb/fixture');
$checks=0;
function verify_bootstrap($condition){++$GLOBALS['checks'];if(!$condition)throw new RuntimeException('Public provider contract failed');}
verify_bootstrap($options['release_provider']('https://github.com/deckerweb/fixture','fixture/fixture.php')===null);
verify_bootstrap($options['release_provider']('https://github.com/deckerweb/other','fixture/fixture.php')===null);
$GLOBALS['deckerweb_library_runtime_v1']=new class {
 public function updater_release($repo,$file,$fresh){return false;}
};
verify_bootstrap($options['release_provider']('https://github.com/deckerweb/fixture','fixture/fixture.php')===false);
$GLOBALS['deckerweb_library_runtime_v1']=new stdClass();
verify_bootstrap($options['release_provider']('https://github.com/deckerweb/fixture','fixture/fixture.php')===null);
echo json_encode(['checks'=>$checks,'failures'=>[],'php'=>PHP_VERSION])."\n";

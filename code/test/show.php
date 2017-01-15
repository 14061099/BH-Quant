<?php
/**
 * Created by PhpStorm.
 * User: zengyutao
 * Date: 2017/1/3
 * Time: 21:10
 */
$StartTime = microtime();
passthru("python ~/api/code/test/main.py",$ans);
$StopTime = microtime();

$StartMicro = substr($StartTime, 0, 10);
$StartSecond = substr($StartTime, 11, 10);
$StopMicro = substr($StopTime, 0, 10);
$StopSecond = substr($StopTime, 11, 10);
$start = floatval($StartMicro) + $StartSecond;
$stop = floatval($StopMicro) + $StopSecond;
$TimeSpent = $stop - $start;
//echo round($TimeSpent, 8) . '秒\n';

$file = file_get_contents("./huice.json");
$json = json_decode($file);
echo $json;
?>


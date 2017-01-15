<?php
/**
 * Created by PhpStorm.
 * User: zengyutao
 * Date: 17-1-12
 * Time: 上午10:34
 */

$StartTime = microtime();
exec("/usr/bin/python ./1-12_19-00/main.py",$array,$ans);
$StopTime = microtime();

$StartMicro = substr($StartTime, 0, 10);
$StartSecond = substr($StartTime, 11, 10);
$StopMicro = substr($StopTime, 0, 10);
$StopSecond = substr($StopTime, 11, 10);
$start = floatval($StartMicro) + $StartSecond;
$stop = floatval($StopMicro) + $StopSecond;
$TimeSpent = $stop - $start;
#echo round($TimeSpent,8).'秒\n';


var_dump(end($array));

?>


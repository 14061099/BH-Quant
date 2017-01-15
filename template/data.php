<?php
$StartTime = microtime();
$xx = exec(".\\test\\1-12_19-00\\main.py", $array, $ans);
echo $ans;
echo "<br>";
foreach ($array as $key => $value) {
	echo $value;
	echo "<br>";
}
$StopTime = microtime();

$StartMicro = substr($StartTime, 0, 10);
$StartSecond = substr($StartTime, 11, 10);
$StopMicro = substr($StopTime, 0, 10);
$StopSecond = substr($StopTime, 11, 10);
$start = floatval($StartMicro) + $StartSecond;
$stop = floatval($StopMicro) + $StopSecond;
$TimeSpent = $stop - $start;
// $chartJson = json_decode(end($array), true);
// echo "1";
?>
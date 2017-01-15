<?php
/**
 * Created by PhpStorm.
 * User: zengyutao
 * Date: 17-1-12
 * Time: 上午10:34
 */

$StartTime = microtime();
$xx = exec("main.py", $array, $ans);
// echo $ans;
// foreach ($array as $key => $value) {
// 	echo $value;
// }
$StopTime = microtime();

$StartMicro = substr($StartTime, 0, 10);
$StartSecond = substr($StartTime, 11, 10);
$StopMicro = substr($StopTime, 0, 10);
$StopSecond = substr($StopTime, 11, 10);
$start = floatval($StartMicro) + $StartSecond;
$stop = floatval($StopMicro) + $StopSecond;
$TimeSpent = $stop - $start;

$json = json_decode(end($array), true);
// echo $json;

// echo "['" . implode("','", $json["date"]) . "']";
// echo "[" . implode(",", $json["val"]) . "]";

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>投资金额视图</title>
    <script src="echarts.js"></script>
</head>
<body>
<div id="main" style="width: 600px;height:400px;margin-left: auto; margin-right: auto;"></div>
<script type="text/javascript">
    var myChart = echarts.init(document.getElementById('main'));
    var option = {
        title: {
            text: '投资金额视图'
        },
        tooltip: {},
        legend: {
            data:["金额"]
        },
        xAxis: {
            data: <?php echo "['" . implode("','", $json["date"]) . "']"; ?>
        },
        yAxis: {},
        series: [{
            name: '金额',
            type: 'line',
            data: <?php echo "[" . implode(",", $json["val"]) . "]"; ?>
        }]
    };
    myChart.setOption(option);
</script>
</body>
</html>
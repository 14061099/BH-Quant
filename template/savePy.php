<?php
//这个不指定文件名
// $str = $_POST['pyname'];
// $format = mb_detect_encoding($str);
// if ($format == 'UTF-8') {
// 	$str = iconv('UTF-8', 'gb2312', $str);
// }
// $pyname = $str . ".py";
// $text = $_POST['text'];
// file_put_contents($pyname, $text);
// file_put_contents("name.py", $pyname);

//这个指定文件�?
$text = $_POST['text'];
file_put_contents("../code/strategy/strategy.py", $text);
?>


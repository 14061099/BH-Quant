<?php
$xx = exec("python ../code/main.py 2>&1", $array, $ans);
var_dump($array);

$chartJson = json_decode(end($array), true);
?>
   
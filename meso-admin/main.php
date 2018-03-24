<?php
$path = './';
$filename = 'test.sh';
if(isset($_GET['temperature'])) {
	//$data = $_GET['temperature'];
	//$output = shell_exec($path . $filename . ' ' . $data);
	$output = shell_exec('./test.sh');
	echo "<pre>$output</pre>";
	
} else {
	echo 'Error!';
}

?>
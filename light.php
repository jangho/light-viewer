Amount Inserted: 
<?php 

echo $_GET["light"];
$filename="light.txt";
$data=$light;
file_put_contents ( $filename , $data);



?>
Success!

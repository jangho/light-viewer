Amount Inserted: 
<?php 

echo $_GET["userX"];
echo $_GET["userY"];
echo $_GET["direction"];

$userX = $_GET["userX"];

$userY = $_GET["userY"];
$direction = $_GET["direction"];

$filename="user.txt";
echo "<br/>";
$data=$userX . "\n" . $userY . "\n" . $direction;
echo $data;
file_put_contents ( $filename , $data  );



?>
Success!

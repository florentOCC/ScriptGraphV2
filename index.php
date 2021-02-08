<html>
<body>
<form action="script.php">
	<input type="submit" value="Graph">
</form>
<?php
if ($dir = opendir(".")) {
  while($file = readdir($dir)) {
    echo "<a href=\"./$file\">$file</a><br>\n";
  }
  closedir($dir);
}
?>
</body>
</html>

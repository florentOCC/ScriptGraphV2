<html>
<body>
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

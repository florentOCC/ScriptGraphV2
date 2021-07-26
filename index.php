<html>
<body>
<form action="script.php">
        <input type="submit" value="Graph">
</form>
<?php
if ($dir = opendir(".")) {
  while($file = readdir($dir)) {
    if( strstr($file, "dot") || $file == "." || $file == ".." || strstr($file, "php") || strstr($file, "hta") || strstr($file, "htp"))
    {
    }
    else
    {
      echo "<a href=\"./$file\">$file</a><br>\n";
    }
  }
  closedir($dir);
}
?>
</body>
</html>

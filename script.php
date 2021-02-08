<?php
#$output = shell_exec("sudo -u apache python /root/ScriptGraphV2-main/graphV2.py");
#system("sudo -u apache python /root/ScriptGraphV2-main/graphV2.py");
#$output = shell_exec('echo yolo');
#echo "<pre>$output</pre>";


$command = escapeshellcmd('sudo /root/ScriptGraphV2-main/graphV2.py');
shell_exec($command);
echo $output;
echo '<p><a href="javascript:history.go(-1)" title="Return to previous page">&laquo; Go back</a></p>';
?>

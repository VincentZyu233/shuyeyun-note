```powershell
$Env:HTTP_PROXY = "http://127.0.0.1:7890"
$Env:HTTPS_PROXY = "http://127.0.0.1:7890"
Invoke-WebRequest -Uri "https://www.google.com" -Method Head -UseBasicParsing

$Env:HTTP_PROXY = "http://192.168.31.84:7890"
$Env:HTTPS_PROXY = "http://192.168.31.84:7890"
Invoke-WebRequest -Uri "https://www.google.com" -Method Head -UseBasicParsing

$Env:HTTP_PROXY = $null
$Env:HTTPS_PROXY = $null
```
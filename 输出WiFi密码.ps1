$profiles = (netsh wlan show profiles) | Select-String "所有用户配置文件" 
foreach ($profile in $profiles) 
{
    $profileStr = $profile.ToString()
    $index = $profileStr.IndexOf(":")
    $wifiName = $profileStr.Substring($index + 1).Trim()
    
    $passwordLine = ((netsh wlan show profile name=$wifiName key=clear) | Select-String "关键内容").ToString()
    $index = $passwordLine.IndexOf(":")
    $password = $passwordLine.Substring($index + 1).Trim()    #WiFi名称里有冒号就不对了

    Write-Output "Wi-Fi名称: $wifiName,  密码: $password"
}



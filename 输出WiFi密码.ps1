$profiles = netsh wlan show profiles | Select-String "所有用户配置文件" 
foreach ($profile in $profiles) 
{
    $profileStr = $profile.ToString()
    $index = $profileStr.IndexOf(":")
    $wifiName = $profileStr.Substring($index + 1).Trim()
    
    $wifiInfo = netsh wlan show profile name=$wifiName key=clear
    if (($wifiInfo | Select-String "安全密钥").ToString().Split(":")[1].Trim() -eq "存在")
    {
        $passwordLine = ($wifiInfo | Select-String "关键内容").ToString()
        $index = $passwordLine.IndexOf(":")
        $password = $passwordLine.Substring($index + 1).Trim()
    
        Write-Output "Wi-Fi名称: $wifiName,  密码: $password"
    }
}



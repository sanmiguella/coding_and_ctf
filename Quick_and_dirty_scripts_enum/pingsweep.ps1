$ipRange = 1..254
$networkAddr = '192.168.2.'
$outPath = 'output.txt'

# Source:
# https://www.checkyourlogs.net/ping-sweep-using-powershell-quick-and-dirty-powershell-mvphour/

foreach($ip in $ipRange) {
    $ipAddr = "$networkAddr$ip"
    $test = Test-Connection -ComputerName $ipAddr -count 1 -Quiet
    $message = "$ipAddr : $test"
    
    Add-Content $outPath -Value $message
    Write-Host $message 
}    
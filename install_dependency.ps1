# powershell 7 installation script
$powerShellInstallerUrl = "https://github.com/PowerShell/PowerShell/releases/download/v7.4.6/PowerShell-7.4.6-win-x86.msi"
$powerShellInstallerPath =  ".\temp\powerShell-installer.msi"
write-output "Downloading powerShell installer..."
Invoke-WebRequest $powerShellInstallerUrl -OutFile $powerShellInstallerPath
Write-Output "Running powerShell installer..."
Start-Process $powerShellInstallerPath
Write-Output "press 'Enter Key' only after installing powerShell :)"
Pause

# python installation script
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe"
$pythonInstallerPath =  ".\temp\python-installer.exe"
write-output "Downloading Python installer..."
Invoke-WebRequest $pythonInstallerUrl -OutFile $pythonInstallerPath
Write-Output "Please remember to tickmark pip in installation !!!"
Pause
Write-Output "Running Python installer..."
Start-Process $pythonInstallerPath
Write-Output "press 'Enter Key' only after installing python :)"
Pause

# FFmpeg.exe Dowloader script
$FFmpegArchiveUrl = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip"
$FFmpegArchivePath = ".\temp\FFmpeg-Archive.zip"
write-output "Downloading FFmpeg Archive..."
Invoke-WebRequest $FFmpegArchiveUrl -OutFile $FFmpegArchivePath
Write-Output "Extracting FFmpeg Archive..."
Expand-Archive $FFmpegArchivePath -DestinationPath "Dependencies\FFmpeg-Sorce"
Write-Output "FFmpeg Archive has been extracted..."

# yt-dlp.exe Dowloader script
$Yt_DlpArchiveUrl = "https://github.com/yt-dlp/yt-dlp/releases/download/2024.10.22/yt-dlp_win.zip"
$Yt_DlpArchivePath = ".\temp\Yt-Dlp-Archive.zip"
write-output "Downloading Yt-Dlp Archive..."
Invoke-WebRequest $Yt_DlpArchiveUrl -OutFile $Yt_DlpArchivePath
Write-Output "Extracting Yt-Dlp Archive..."
Expand-Archive $Yt_DlpArchivePath -DestinationPath "Dependencies\Yt-Dlp-Sorce"
Write-Output "Yt-Dlp Archive has been extracted..."

#selenium install and temp cleanup script
python -m pip install selenium
Remove-Item temp\*

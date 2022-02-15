# Research environment setup : Windows & Softwares
## 1. Initialization : Install windows
1. Create a windows installation usb
2. Format all the partitions and install windows on the SSD
3. Make sure **not** to login by ms account. Rather make a **local** account with _english_ name (using the menu on the bottom left)
4. When you see DESKTOP check if all the storages are properly registered, else check partition settings

Size | cluster size
-----|------
~4GB | 2kb
~8GB | 4kb
~16GB | 8kb
~32GB | 16kb
~64GB | 32kb
~128GB | 64kb
~256GB | 128kb
~512GB | 256kb
~1024GB | 512 kb
~2048GB | 1024kb

## 2. Core program installation
> If these programs / fuctions does not work properly, it's better to reinstall Windows...

1. Install Chrome
2. Install vs code
   1. Install extensions
      1. Docker family
      2. Remote family (SSH)
   2. Check ssh connection
      1. silws@165.132.128.243:22
      2. user@165.132.128.241:22
   3. Open a new/running container
      1. For docker command, check [docker_commands.md]
      2. Right click => Attach VS Code, on the running container

**(Optional: wsl2)**
1. Install Windows terminal
2. Install Powershell
3. Activate WSL2 in Powershell
   1. dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   2. dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart 
   3. _Reboot PC_
   4. wsl
4. Install linux kernel update [https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi]
5. Install Ubuntu
   1. Set UNIX name/pw
6. Set wsl version
   1. version check : wsl -l -v
   2. version change : wsl --set-version Ubuntu 2
   3. default change : wsl --set-default-version 2

## 3. Other suggested programs
- Drivers
  - 3Dp-chip
  - CPU
  - Chipset
  - Grapic Driver
  - Audio
- MS office
- Adobe
  - Ps
  - Pr
  - Ae
  - Acrobat pro
- Hangul
- Git
- Pytorch
  - CUDA 11.3
  - cudnn 11.X
  - python 3.9
- Util
  - Bandi_zip
  - Pot player
  - OBS
  - Zoom
  - Anydesk
  - Carnac
  - Endnote
  - Putty
  - Everything
  - nPDF
- Kakaotalk
- Blender
- Google drive
- Matlab
- Fonts
  - Fira Code (Nerd Font)
  - Hack (Nerd Font)
  - D2Coding
- VS code Extensions
  - Themes
    - One Dark Pro
    - Tokyo Night
    - Material Icon
    - Peacock
  - Git related
    - Gitlens
    - Git Graph
    - Git Blame
    - Gitignore
    - Git History
  - Utility
    - Tag-related stuff
    - Bracket pair colorizer
    - CodeSnap
    - Prettier
    - Path Intellisense
    - Visual Studio IntelliCode
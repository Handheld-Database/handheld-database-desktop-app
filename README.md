# Application to make the contribution to the Handheld Database easier.

## About
This application is **work in progress**. You will be able to use it to add Platforms, Systems and Games to those systems. You will be able to do everything visually, like now through the scripts.

## TO DO
- [x] Make temporary UI for the Platfrom, System and Game windows
- [ ] Make temporary UI for the manual game and automatic game contribution.
- [x] Put all classes in different files.
- [ ] Make a function to dynamically read the existing platforms and the systems in those platforms and make a dropdown menu using them.
- [ ] Implement all the functionality that exists in the scripts.
- [ ] Clean up the folders (duplicate scripts, etc...).
- [ ] Make a test build off the application. For Windows and Linux.

## Making an executable

**My Antivirus detects it as a virus, it's most likely because the .exe isn't signed. Need to be solved later, maybe I can self-sign it with OpenSSL or something.**

To make an executable and include the images in the file:
- to not have a console
- to have only one .exe file
- if you want to have pictures in your program and have them in the exe file, you need to specify their path.
- (python -m PyInstaller , is used because I didn't set the PATH correctly.)

python -m PyInstaller --onefile --noconsole --name 'Application Name' --add-data .\desktop_app\images\favicon.ico:. --add-data .\desktop_app\images\platform.png:. --add-data .\desktop_app\images\system.png:. --add-data .\desktop_app\images\game.png:. --add-data .\desktop_app\images\add.png:. --add-data .\desktop_app\images\import.png:. .\desktop_app\main.py


rmdir dist /s /q
rmdir build /s /q
pyinstaller ..\deflate_folder.py
copy dist\deflate_folder\*.* . /Y
pause
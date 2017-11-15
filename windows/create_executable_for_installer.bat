rmdir dist /s /q
rmdir build /s /q
pyinstaller ..\install.py
copy dist\install\*.* . /Y
pause
import os
import subprocess
import shutil
import requests
import ctypes
import time

if not os.path.isdir('C:/SystemFILE'):
    os.mkdir('C:/SystemFILE')

os.chdir('C:/SystemFILE')
print(f"Please wait...")
  
response = requests.get(url='https://www.iconarchive.com/download/i120869/iconarchive/treasure-chest/Skull.ico')
with open('rat.ico', 'wb') as file:
    file.write(response.content)

response = requests.get(url='https://c4.wallpaperflare.com/wallpaper/197/694/419/technology-hacker-anonymous-wallpaper-thumb.jpg')
with open('wallper.jpg', 'wb') as file:
    file.write(response.content)
time.sleep(5)

file = open('Sudo.py', 'w')
file.write('''print("Hi")
for i in range(0, 30):
    s = input("You Are Hacked!!!\\n")
for i in range(0, 30):
    print("AXAXAAXXAXAAXAXAXAXXAAXAXAXAXAXAXAX\n")''')
file.close()
print('35% ready')

subprocess.run('pip install pyinstaller', shell=True)

subprocess.run('pyinstaller -F -i "rat.ico" Sudo.py', shell=True)

time.sleep(3)
shutil.copy('dist/Sudo.exe', 'C:/Users/Admin/Desktop/')
os.chdir('C:/Users/Admin/Desktop/')
print("80% ready")

os.startfile('Sudo.exe')
print("100% ready")
time.sleep(1)
print("Thanks for waiting!\nNow pay attention to the desktop where your application is, launch and have fun!!!")
ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\SystemFILE\wallper.jpg', 0)
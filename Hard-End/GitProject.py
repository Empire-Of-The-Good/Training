import os
import subprocess
import time
import pyautogui

path_git = 'C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe'
path_ssh = 'C:/Users/Admin/.ssh'

niсk = input('You\'r nick...\n')
gmail = input('Your mail...\n')
profil_nic = f'git config --global user.name "{niсk}" '
profil_mail = f'git config --global user.email {gmail}'
key_ssh = f'ssh-keygen -t ed25519 -C "{gmail}"'

os.startfile(path_git)
time.sleep(7)
try:
    lists = os.listdir(path_ssh)

    for file in lists:
        itog = os.path.join(path_ssh, file)
        if os.path.isfile(itog):
            os.remove(itog)
except:
    pass

subprocess.run(profil_nic, shell=True)
subprocess.run(profil_mail, shell=True)
subprocess.run(key_ssh, shell=True)

subprocess.run('clip < ~/.ssh/id_ed25519.pub', shell=True)
try:
    subprocess.run('cat ~/.ssh/id_ed25519.pub', shell=True)
except:
    pass
subprocess.run('ssh -T git@github.com ', shell=True)
time.sleep(1)
pyautogui.typewrite('yes\n')
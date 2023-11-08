import string
import subprocess


def checking(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="UTF-8")
    out = result.stdout
    if result.returncode == 0:

        cleaned_text = ''.join(char for char in out if char not in string.punctuation)
        print(cleaned_text)
        if text in cleaned_text:
            return True
        else:
            return False
    return f'wrong command'


if __name__ == '__main__':
    print(checking('cat /etc/os-release', 'NAME'))
    print(checking('ls /home/user', 'Видео'))
import os
def say(msg = "akhir", voice = "Damayanti"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

import os
def say(msg = "จบ", voice = "Kanya"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

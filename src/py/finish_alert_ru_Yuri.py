import os
def say(msg = "конец", voice = "Yuri"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

import os
def say(msg = "τέλος", voice = "Melina"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

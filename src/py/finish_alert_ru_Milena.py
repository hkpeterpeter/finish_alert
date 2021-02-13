import os
def say(msg = "конец", voice = "Milena"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

import os
def say(msg = "fim", voice = "Joana"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

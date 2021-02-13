import os
def say(msg = "slutt", voice = "Nora"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

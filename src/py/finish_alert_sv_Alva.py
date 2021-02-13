import os
def say(msg = "slutet", voice = "Alva"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

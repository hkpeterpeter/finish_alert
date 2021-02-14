import os
def say(m = "slutet", v = "Alva"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()

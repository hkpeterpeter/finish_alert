import os
def say(m = "fim", v = "Luciana"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()

import os
def say(msg = "finir", voice = "Amelie"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

import os
def say(msg = "終わり", voice = "Kyoko"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()

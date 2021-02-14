import os
def say(m = "終わり", v = "Kyoko"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()

import os
def say(m = "Finish", v = "Victoria"):
    os.system(f'say -v {v} {m}')   # say (Mac only)

if __name__ == "__main__":
    # Usage: after running some codes, alert yourself
    say()                              # English
    say(m="完了吧，如無意外",v="Sin-ji")  # Cantonese
    say(m="完結",v="Ting-Ting")         # Chinese
    say(m="終わり",v="Kyoko")           # Japanese
    say(m="종료",v="Yuna")              # Korean
    say(m="fin",v="Monica")            # Spanish
    say(m="finir",v="Amelie")          # French

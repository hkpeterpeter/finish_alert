# finish_alert

Programs may run for a long time. It is useful to say something when the program is finished. 

## macOS

- [Say](https://ss64.com/osx/say.html) converts text to audible speech. 

### Python 

```python
# List of voices: say -v ?
import os
def say(m = "Finish", v = "Victoria"):
    os.system(f'say -v {v} {m}')
```

Usage: 

```python
say()                              # English
say(m="完了吧，如無意外",v="Sin-ji")  # Cantonese
say(m="完結",v="Ting-Ting")         # Chinese
say(m="終わり",v="Kyoko")           # Japanese
say(m="종료",v="Yuna")              # Korean
say(m="fin",v="Monica")            # Spanish
say(m="finir",v="Amelie")          # French
```

## Other Languages

`say` function with different default values for the supporting human languages can be founded in [src/py](src/py)

### Chinese
```python
import os
def say(m = "完結", v = "Ting-Ting"):
    os.system(f'say -v {v} {m}')
```

### Cantonese

```python
import os
def say(m = "完結", v = "Sin-ji"):
    os.system(f'say -v {v} {m}')
```

### Spanish
```python
import os
def say(m = "fin", v = "Juan"):
    os.system(f'say -v {v} {m}')
```

### Japanese
```python
import os
def say(m = "終わり", v = "Kyoko"):
    os.system(f'say -v {v} {m}')
```

### Korean
```python
import os
def say(m = "종료", v = "Yuna"):
    os.system(f'say -v {v} {m}')
```
   
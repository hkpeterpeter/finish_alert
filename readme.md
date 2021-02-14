# finish_alert

Programs may run for a long time. 
It is useful to say something when the program finished. 

Here are some useful gists:

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
# Run your program/experiment...
say() # say finish at the end

# Or say something more exciting
say("Great! Finally finished, please check the result!") 

# Or switch to another voice
say("Great!", "Alex")
```

## Other Languages

Code examples for other human languages can be founded in [src/py](src/py)

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
   
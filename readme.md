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
def say(msg = "Finish", voice = "Victoria"):
    os.system(f'say -v {voice} {msg}')
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
def say(msg = "完結", voice = "Ting-Ting"):
    os.system(f'say -v {voice} {msg}')
```

### Cantonese

```python
import os
def say(msg = "完結", voice = "Sin-ji"):
    os.system(f'say -v {voice} {msg}')
```

### Spanish
```python
import os
def say(msg = "fin", voice = "Juan"):
    os.system(f'say -v {voice} {msg}')
```

### Japanese
```python
import os
def say(msg = "終わり", voice = "Kyoko"):
    os.system(f'say -v {voice} {msg}')
```

### Korean
```python
import os
def say(msg = "종료", voice = "Yuna"):
    os.system(f'say -v {voice} {msg}')
```
   
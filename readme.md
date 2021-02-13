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
Code examples for other human languages can be founded in [src/py](src/py)
- For example: `finish_alert_ja_Kyoko.py` uses Japanese Yuna voice with default message `終わり`

Usage:

```python
# Run your program/experiment...
say() # say finish at the end

# Or say something more exciting
say("Great! Finally finished, please check the result!") 

# Or switch to another voice
say("Great!", "Alex")
```
   
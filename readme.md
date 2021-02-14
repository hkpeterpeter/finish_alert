# finish_alert

Programs may run for a long time. It is useful to say something when the program is finished. 

## macOS

- [Say](https://ss64.com/osx/say.html) converts text to audible speech. 

### Python 

```python
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

### Go 

```go
import "os/exec"

func say(m string, v string) {
	if m == "" {
		m = "Finish"
	}
	if v == "" {
		v = "Victoria"
	}
	exec.Command("say", "-v", v, m).Run()
}
```

Usage: 
```go
say("", "")                    // English
say("完了吧，如無意外", "Sin-ji") // Cantonese
say("完結", "Ting-Ting")        // Chinese
say("終わり", "Kyoko")          // Japanese
say("종료", "Yuna")             // Korean
say("fin", "Monica")           // Spanish
say("finir", "Amelie")         // French
```

## Default languages in Python

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
   
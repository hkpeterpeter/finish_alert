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

Usage in Python: 

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
	exec.Command("say", "-v", v, m).Run()
}
```

Usage in Go: 
```go
say("Finish", "Victoria")       // English
say("完了吧，如無意外", "Sin-ji") // Cantonese
say("完結", "Ting-Ting")        // Chinese
say("終わり", "Kyoko")          // Japanese
say("종료", "Yuna")             // Korean
say("fin", "Monica")           // Spanish
say("finir", "Amelie")         // French
```

### NodeJS

```js
// By default, Javascript runs in a parallel (async/await is needed)
const util = require('util');
const exec = util.promisify(require('child_process').exec);
async function say(m = "Finish", v = "Victoria") {
  await exec(`say -v ${v} ${m}`) 
}
```

Usage in NodeJS:
```js
// Note: without using async/await, 
// all sentences will be spoken at the same time
async function main() {
  await say()                              // English
  await say(m="完了吧，如無意外",v="Sin-ji")  // Cantonese
  await say(m="完結",v="Ting-Ting")         // Chinese
  await say(m="終わり",v="Kyoko")           // Japanese
  await say(m="종료",v="Yuna")              // Korean
  await say(m="fin",v="Monica")            // Spanish
  await say(m="finir",v="Amelie")          // French
}
main()
```

### C/C++

```c++
#include <stdio.h>
#include <stdlib.h>

void say(char *m, char *v) {
    char cmd[1000];
    sprintf(cmd, "say -v %s %s\n", v, m);
    system(cmd);
}
```

Usage in C/C++:

- Tool: [https://onlineutf8tools.com/convert-utf8-to-bytes](https://onlineutf8tools.com/convert-utf8-to-bytes)
- Reference: [https://unicodebook.readthedocs.io/programming_languages.html](https://unicodebook.readthedocs.io/programming_languages.html)

```c++
int main() {
    // UTF-8 needs to convert to bytes
    say("Finish","Victoria");  // English
    say("\xe5\xae\x8c\xe7\xb5\x90", "Sin-ji"); // Cantonese
    say("\xe5\xae\x8c\xe7\xb5\x90", "Ting-Ting"); // Chinese
    say("\xe7\xb5\x82\xe3\x82\x8f\xe3\x82\x8a", "Kyoko"); // Japanese
    say("\xec\xa2\x85\xeb\xa3\x8c","Yuna"); // Korean
    say("fin","Monica"); // Spanish
    say("finir","Amelie"); // French
    return 0;
}
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
   
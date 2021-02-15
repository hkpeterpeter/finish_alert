# finish_alert

Programs may run for a long time. It is useful to say something when the program is finished in macOS.

[Python](#Python) [Go](#Go) [NodeJS](#NodeJS) [C/C++](#cc) [Java](#Java) [VanillaJS](#VanillaJS)

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
    say("Finish","Victoria");                              // English
    say("\xe5\xae\x8c\xe7\xb5\x90", "Sin-ji");             // Cantonese
    say("\xe5\xae\x8c\xe7\xb5\x90", "Ting-Ting");          // Chinese
    say("\xe7\xb5\x82\xe3\x82\x8f\xe3\x82\x8a", "Kyoko");  // Japanese
    say("\xec\xa2\x85\xeb\xa3\x8c","Yuna");                // Korean
    say("fin","Monica");                                   // Spanish
    say("finir","Amelie");                                 // French
    return 0;
}
```

### Java

```java
public class Say 
{
    public static void say(String m, String v) throws Exception {
        String cmd = "say -v " + v + " " + m;
        Runtime.getRuntime().exec(cmd).waitFor(); // wait until it finishes  
    }
}
```

Usage in Java:
```java
Say.say("Finish","Victoria");        // English
Say.say("完了吧，如無意外", "Sin-ji"); // Cantonese
Say.say("完結", "Ting-Ting");        // Chinese
Say.say("終わり", "Kyoko");          // Japanese
Say.say("종료", "Yuna");             // Korean
Say.say("fin", "Monica");           // Spanish
Say.say("finir", "Amelie");         // French  
```

### VanillaJS 

- Using the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API#speech_synthesis)
- Note: speechSynthesis.speak() without user activation is no longer allowed since M71, around December 2018.
- See [https://www.chromestatus.com/feature/5687444770914304](https://www.chromestatus.com/feature/5687444770914304) for more details

- Implementation: [src/vanilla_js](src/vanilla_js)

```js
// say.js (vanilla)
let voices = []; // store the voices
let synth = window.speechSynthesis;

function say(m = "Finish", v = "Victoria") {
    const speak = () => {
        let utterThis = new SpeechSynthesisUtterance(m);
        for ( let voice of voices ) {
            if ( voice.name === v ) {
                utterThis.voice = voice;
                break;
            }
        }
        synth.speak(utterThis);
    }
    if ( voices.length === 0 ) {  // For the first time without a voice list
        // Note: synth.getVoices() - use setInterval trick to get the voice list from the server
        let id = setInterval(() => {
            voices = synth.getVoices();
            if (voices.length !== 0) {
                clearInterval(id);
                speak();
            }
        }, 10);
    } 
    else { // call the speak() handler if the voice list is ready
        speak();
    }
}
```

Usage in Vanilla JS
```js
<script src="say.js"></script>
<button onclick="say('Finish','Victoria');">English</button> 
<button onclick="say('完了吧，如無意外','Sin-ji');" >Cantonese</button>
<button onclick="say('完結','Ting-Ting');">Chinese</button>
<button onclick="say('終わり','Kyoko');">Japanese</button>
<button onclick="say('종료','Yuna');">Korean</button>
<button onclick="say('fin','Monica');">Spanish</button>
<button onclick="say('finir','Amelie');">French</button>
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
   
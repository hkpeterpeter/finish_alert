package main

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

func main() {
	say("", "")               // English
	say("完了吧，如無意外", "Sin-ji") // Cantonese
	say("完結", "Ting-Ting")    // Chinese
	say("終わり", "Kyoko")       // Japanese
	say("종료", "Yuna")         // Korean
	say("fin", "Monica")      // Spanish
	say("finir", "Amelie")    // French
}

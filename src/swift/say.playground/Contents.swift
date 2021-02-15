import Foundation

func say(m: String, v: String) {
    let p = Process()
    p.executableURL = URL(fileURLWithPath: "/usr/bin/env")
    p.arguments = ["say", "-v", v, m]
    do {
        try p.run()
        p.waitUntilExit()
    } catch {
        print("Unexpected error: \(error).")
    }
}

say(m:"Finish", v:"Victoria")     // English
say(m:"完了吧，如無意外",v:"Sin-ji") // Cantonese
say(m:"完結",v:"Ting-Ting")        // Chinese
say(m:"終わり",v:"Kyoko")          // Japanese
say(m:"종료",v:"Yuna")             // Korean
say(m:"fin",v:"Monica")           // Spanish
say(m:"finir",v:"Amelie")         // French



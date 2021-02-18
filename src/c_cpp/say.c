#include <stdio.h>
#include <stdlib.h>

void say(char *m, char *v) {
    char cmd[1000];
    sprintf(cmd, "say -v %s %s\n", v, m);
    system(cmd);
}

// u8 prefix: (UTF-8) encoding is needed for non-ASCII string 
int main() {
    say("Finish","Victoria");               // English
    say(u8"完了吧，如無意外", "Sin-ji");       // Cantonese
    say(u8"完結", "Ting-Ting");              // Chinese
    say(u8"終わり", "Kyoko" );               // Japanese
    say(u8"종료","Yuna");                    // Korean
    say("fin","Monica");                    // Spanish
    say("finir","Amelie");                  // French 
    return 0;
}
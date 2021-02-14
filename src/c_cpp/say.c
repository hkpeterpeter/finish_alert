#include <stdio.h>
#include <stdlib.h>

void say(char *m, char *v) {
    char cmd[1000];
    sprintf(cmd, "say -v %s %s\n", v, m);
    system(cmd);
}

int main() {
    // UTF-8 needs to convert to bytes
    // Tool: https://onlineutf8tools.com/convert-utf8-to-bytes
    // Reference: https://unicodebook.readthedocs.io/programming_languages.html

    say("Finish","Victoria");
    say("\xe5\xae\x8c\xe4\xba\x86\xe5\x90\xa7\xef\xbc\x8c\xe5\xa6\x82\xe7\x84\xa1\xe6\x84\x8f\xe5\xa4\x96", "Sin-ji");
    say("\xe5\xae\x8c\xe7\xb5\x90", "Ting-Ting");
    say("\xe7\xb5\x82\xe3\x82\x8f\xe3\x82\x8a", "Kyoko");
    say("\xec\xa2\x85\xeb\xa3\x8c","Yuna");
    say("fin","Monica");
    say("finir","Amelie");

    return 0;
}
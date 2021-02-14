import os
from subprocess import Popen, PIPE

# Note: translated using Google translate

msg = {}
msg["zh"] = msg["hk"] = "完結"
msg["en"] = "Finish"
msg["ja"] = "終わり"
msg["ko"] = "종료"
msg["it"] = "fine"
msg["sv"] = "slutet"
msg["fr"] = "finir"
msg["de"] = "Ende"
msg["he"] = "סוֹף"
msg["id"] = "akhir"
msg["es"] = "fin"
msg["nl"] = "einde"
msg["ro"] = "Sfârșit"
msg["pt"] = "fim"
msg["th"] = "จบ"
msg["sk"] = "koniec"
msg["hi"] = "समाप्त"
msg["ar"] = "نهاية"
msg["hu"] = "vége"
msg["el"] = "τέλος"
msg["ru"] = "конец"
msg["nb"] = "slutt"
msg["da"] = "ende"
msg["fi"] = "loppuun"
msg["tr"] = "son"
msg["pl"] = "koniec"
msg["cs"] = "konec"

# extracted text from: say -v ?

voice_lines = Popen(["say","-v","?"], stdout=PIPE).communicate()[0].decode('utf-8')

code_template = """\
import os
def say(m = "%s", v = "%s"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
"""

voice_lines = voice_lines.strip()

# Parse [Voice  code] from the lines
voice_code_list = [ line.split("#")[:-1][0].strip().split() for line in voice_lines.split("\n") ]

for voice_code in voice_code_list:
    voice = voice_code[0]
    lang = voice_code[1].split("_")[0]
    if lang in msg:
        # filenames of the python source files
        fname = f"src/py/finish_alert_{lang}_{voice}.py"

        # Generated code
        code_generated = code_template % (msg[lang], voice)

        with open(fname, "w") as f:
            f.write(code_generated)

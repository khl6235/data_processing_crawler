import json
import csv

vid = "0015551"
personId = "0089"

i_file_path = f'./라벨링데이터/VID_{vid}_person_{personId}.json'
o_file_path = f'VID_{vid}_person_{personId}.csv'
with open(i_file_path, 'r') as i_file, open(o_file_path, 'w', newline='') as o_file:
    data = json.load(i_file)
    texts = data['annotations']['text']
    f = csv.writer(o_file, csv.QUOTE_NONE)
    f.writerow(['No', '문장', '주어', '목적어', '동사', '관계성', '명령어'])
    i = 1
    for text in texts:
        subj = text['subject'] if text['subject'] else ""
        obj = text['object'] if text['object'] else ""
        vrb = text['verb'] if text['verb'] else ""
        rlt = text['relation']
        if rlt == "": rlt = "*무관계성"

        front_q = "document.querySelector(\"input[id=outlined-email-input][name="
        back_q = "]\").value = "

        console_cmd = f'{front_q}subject{back_q}"{subj}"'+'\n'
        console_cmd += f'{front_q}object{back_q}"{obj}"'+'\n'
        console_cmd += f'{front_q}verb{back_q}"{vrb}"'+'\n'
        if rlt != "*무관계성":
            console_cmd += f'{front_q}relation{back_q}"{rlt}"'
        
        f.writerow([i, text['korean'], subj, obj, vrb, rlt, console_cmd])
        print(i)
        print(console_cmd)
        i += 1
import dicom
import sys
import os
from dicom import UID
import random, string
from shutil import copyfile
import csv

def create_info_from_csv(csv_file_name,out_dir):
    with open(csv_file_name, 'r') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',', quotechar='|')
        pinfo = {}
        for row in list(csv_data)[1:]:
            print(row)
            pid = row[1]
            age = row[2]
            side = row[2]
            feature = row[3]

            suspic = row[4]
            other = row[5]
            suspic2 = row[6]
            vals = (age,[(side,feature)],suspic,other,suspic2)
            if(pid in pinfo): 
                vals_prev = pinfo[pid]
                if(age!=vals_prev[0]): print("error age vals different")
                if(suspic.isdigit() and vals_prev[2].isdigit() and suspic!=vals_prev[2]): print("error suspicion vals different")
                print(vals[1])
                feats = vals_prev[1] + vals[1]
                if(vals_prev[2].isdigit()): suspic = vals_prev[2]
                vals =(age,feats,suspic, other,suspic2)
            pinfo[pid] = vals
        for pid in pinfo:
            create_info_file(pinfo[pid],out_dir,pid,suspic2,other)
            

def create_info_file(vals,out_dir,pid,suspic2,other):
    age = vals[0]
    feats = vals[1]
    sus = vals[2]
    sus2 = vals[3]
    other = vals[4]
    ptext = "<table><tr><th>Patient Age</th><th>Side affected</th><th>Clinical Feature</th><th>Other Feature</th><th>Clinical Suspicion score</th></tr>"
    def feat_func(side,feat): return "<tr> <td>" + age + "</td> <td>"+ feat + "</td><td>" + sus + " </td>"
    feat_text = ''.join([feat_func(s,f) for s,f in feats])
    sus_text = "<td>" + sus2 + "</td><td>" + other + "</td></tr></table>"
    text = ptext+feat_text +sus_text

    if(str(age)!=None):
        f_abs_path = os.path.join(out_dir,str(pid)+'.info')
        with open(f_abs_path, "w") as text_file:
            text_file.write(text)

        
        
            
def some_func():
    pass

def main():
    csv_file_name = sys.argv[1]
    out_dir = sys.argv[2]
    create_info_from_csv(csv_file_name,out_dir)

if __name__=='__main__':
    main()

import os
import shutil
from_dir="C:/Users/giova/Downloads/PRO_1-1_C102_AtividadeDaProfessora2-main/PRO_1-1_C102_AtividadeDaProfessora2-main"
to_dir="C:/Users/giova/Downloads/Fim"
listoffiles=os.listdir(from_dir)
for file_name in listoffiles:
    name,astencion=os.path.splitext(file_name)
    if astencion in [".pdf"]:
        pasta1=from_dir+"/"+file_name
        pasta2=to_dir+"/"+"imagens"
        pasta3=to_dir+"/"+"imagens"+"/"+ file_name
        if os.path.exists(pasta2):
            print("movendo")
            shutil.move(pasta1,pasta3)
        else:
            os.makedirs(pasta2)
            print("movendo")
            shutil.move(pasta1,pasta3)       
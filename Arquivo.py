import os
import shutil

from_dir = "C:/Users/foco/Downloads"
to_dir = "C:/Users/foco\Pictures/arquivosB"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpn','jpeg','jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Arquivos_Imagem'
        path3 = to_dir + '/' + "Arquivos_Imagem" + '/' + file_name

        #Verifique se o caminho da pasta/diretorio existe
        #caso contrario,crie uma NOVA pasta/diretorio
        if os.path.exists(path2):
            print('Movendo'+ file_name + '....')

            #Mover de path1---->path3
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('movendo' + file_name + '.....')
            shutil.move(path1,path3)    

            
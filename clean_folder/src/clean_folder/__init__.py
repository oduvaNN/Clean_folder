import os 
import shutil 
import sys

  

def normalize(text):
    translit_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie',
                     'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
                     'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
                     'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu',
                     'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 
                     'Є': 'Ie', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'I', 'Й': 'I', 'К': 'K', 
                     'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 
                     'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 
                     'Ь': '', 'Ю': 'Iu', 'Я': 'Ia'}
    
    normalized_text = ""
    rash=os.path.splitext(text)[1]
    for char in os.path.splitext(text)[0]:
        if char.isalpha():
            if char in translit_dict:
                normalized_text += translit_dict[char]
            else:
                normalized_text += char
        elif char.isdigit():
            normalized_text += char
        else:
            normalized_text += "_"
    return normalized_text+rash



'''
def normalize(name): 

    valid_chars = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 

    return ''.join(c for c in name if c in valid_chars) 

'''




def move_file(filename, dest_folder, path): 

    dest_folder = os.path.join(path, dest_folder) 

    if not os.path.exists(dest_folder): 

        os.makedirs(dest_folder) 

    shutil.move(filename, os.path.join(dest_folder, normalize(os.path.basename(filename)))) 

  

def handle_directory(path): 

    for filename in os.listdir(path): #список файлов внутри

        file_path = os.path.join(path, filename) 

        if os.path.isdir(file_path): #если папка, снова вызываем

            handle_directory(file_path) 

        else: 

            file_ext = os.path.splitext(file_path)[1].lower() #если файл, смотрим на расширение

            if file_ext in (".zip", ".gz", ".tar", ".rar"): 

                # Handle archives 

                archive_folder = os.path.join(path, "archives", os.path.splitext(normalize(filename))[0]) #путь к папке архива

                if not os.path.exists(archive_folder): #если папки нет, создаем

                    os.makedirs(archive_folder) 

                shutil.unpack_archive(file_path, archive_folder) 

            elif file_ext in (".jpg", ".png", ".jpeg", ".svg", ".bmp"): 

                move_file(file_path, "images", path) 

            elif file_ext in (".doc", ".pdf", ".txt", ".docx", ".xlsx", ".pptx"): 

                move_file(file_path, "documents", path) 

            elif file_ext in (".mp3", ".wav", ".ogg", ".amr"): 

                move_file(file_path, "audio", path) 

            elif file_ext in (".mp4", ".avi", ".mov", ".mkv"): 

                move_file(file_path, "video", path) 

            else: 

                # Unknown file type, leave it in place 

                pass 

  

    # Delete empty directories 

    if not os.listdir(path): 

        os.rmdir(path) 

  

# Start in the current directory 


def clean():
    handle_directory(sys.argv[1])


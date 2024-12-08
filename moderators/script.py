import requests
import hashlib
import os

def convert(num):
    num_str = str(num)
    hash_md5 = hashlib.md5(num_str.encode()).hexdigest()
    return hash_md5

def download_pdf(log_hash):
    url = f"http://10.10.11.173/logs/{log_hash}/logs.pdf"

    directory = "./logs"
    file_path = os.path.join(directory, f"{log_hash}.pdf")
    
    try:
        os.makedirs(directory, exist_ok=True)
        
        response = requests.get(url)
        response.raise_for_status()
    
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        print(f"Archivo descargado exitosamente en: {file_path}")
    
    except requests.RequestException as e:
        print(f"Error al descargar el archivo: {e}")
    except OSError as e:
        print(f"Error al guardar el archivo: {e}")
    

id_report_v = [9798, 4221, 3478, 7612, 2589, 8121]

for id in id_report_v:
    download_pdf(convert(id))
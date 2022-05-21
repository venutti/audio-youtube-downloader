from pytube import YouTube
import sys

UBICACIONDEFAULT = "/home/lvenutti/Música"

print("Inicializando PyTube")

def descargarAudio(url: str, ubicacion=UBICACIONDEFAULT):
    """Recibe una URL valida por parametro y la descarga en la ubicacion pasada."""
    try:
        yt = YouTube(url)
        video = yt.streams.get_audio_only()
        titulo = video.title
        video.download(ubicacion)
    except:
        print("No se pudo descargar la URL")
        return False
    print(f"DESCARGADO CORRECTAMENTE... {titulo}")
    return True

def descargarDeArchivo(archivo: str):
    with open(archivo, "r") as f:
        for linea in f.readlines():
            descargarAudio(linea)

def main():
    url = True
    if len(sys.argv) > 1:
        print("Descargando videos...")
        for archivo in sys.argv[1:]:
            descargarDeArchivo(archivo)
        return
    while url:
        url = input("Ingrese la URL del video a descargar:").strip()
        descargarAudio(url)
main()

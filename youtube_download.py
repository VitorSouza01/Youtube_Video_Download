
# Youtube Vídeo Download

# Instalando a biblioteca "Pytube".
from pytube import YouTube, streams

# Para inserir o link do vídeo do Youtube.
print("[Download Vídeo do Youtube!]")
link = input("Insira o link do vídeo: ")
video = YouTube(link)

# Para mostrar o título do vídeo e que ja iniciou o download.
print("Titulo = ", video.title)
print("Baixando...")

# Para baixar a maior resolução do vídeo.
stream = video.streams.get_highest_resolution()
stream.download(output_path="D:\Python\Downloads_Youtube")  # Colocar o caminho onde o video será salvo.
print("Download concluído com sucesso!")

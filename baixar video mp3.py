import tkinter as tk
import pytube
import os

# Criar uma janela principal
window = tk.Tk()
window.title("Insira o URL do vídeo")

# Criar uma caixa de texto
text_box = tk.Entry(window, width=150)
text_box.pack()

# Criar um botão "Baixar"
def on_button_click():
  # Obter a URL do vídeo do YouTube da caixa de texto
  url = text_box.get()



  # Criar um objeto YouTube com a URL do vídeo
  yt = pytube.YouTube(url)

  # Selecionar o stream de vídeo mais alto e obter o link de download
  video = yt.streams.filter(only_audio=True).first()
  download_url = video.url
  
  # Baixar o vídeo em MP3
  video.download("C:/Users/Cliente/Music")

  # Renomear o arquivo baixado para que ele tenha a extensão .mp3
  os.rename("C:/Users/Cliente/Music/{}".format(video.default_filename),
            "C:/Users/Cliente/Music/{}.mp3".format(os.path.splitext(video.default_filename)[0]))

button = tk.Button(window, text="OK", command=on_button_click)
button.pack()

window.mainloop()



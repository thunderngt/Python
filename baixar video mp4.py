import tkinter as tk
import pytube
import os

# Criar uma janela principal
window = tk.Tk()
window.title("Insira o URL do vídeo")

# Criar uma caixa de texto
text_box = tk.Entry(window, width=150)
text_box.pack()

# Criar uma caixa de seleção de resolução
resolution_var = tk.StringVar(window)
resolution_var.set("1080p") # Define a resolução padrão para 1080p
resolution_select = tk.OptionMenu(window, resolution_var, "240p", "360p", "480p", "720p", "1080p")
resolution_select.pack()

# Criar um botão "Baixar"
def on_button_click():
  # Obter a URL do vídeo do YouTube da caixa de texto
  url = text_box.get()

  # Criar um objeto YouTube com a URL do vídeo
  yt = pytube.YouTube(url)

  # Obter a resolução selecionada pelo usuário
  resolution = resolution_var.get()

  # Filtrar os streams disponíveis pelo atributo "resolution" e selecionar o primeiro stream com a resolução desejada
  video = yt.streams.filter(only_audio=False, resolution=resolution).first()
  download_url = url
  
  # Baixar o vídeo
  video.download("C:/Users/Cliente/Videos")

  # Renomear o arquivo baixado para que ele tenha a extensão .mp4
  os.rename("C:/Users/Cliente/Videos/{}".format(video.default_filename),
            "C:/Users/Cliente/Videos/{}.mp4".format(os.path.splitext(video.default_filename)[0]))

button = tk.Button(window, text="OK", command=on_button_click)
button.pack()

window.mainloop()
# Este programa tem como objetivo abrir um arquivo PDF e adicionar imagens de rubrica e assinatura
# em páginas específicas. Ele também insere a data atual em uma das páginas.

# Primeiramente, importamos as bibliotecas necessárias:
# - `fitz`: Biblioteca do PyMuPDF usada para manipular o PDF.
# - `cv2`: Biblioteca OpenCV, aqui importada mas não utilizada no código.
# - `PIL.Image`: Biblioteca para manipulação de imagens (importada mas não utilizada).
# - `datetime`: Para inserir a data atual no documento.

import fitz  
import cv2
from PIL import Image
import datetime

# Em seguida, abrimos o arquivo PDF onde as imagens e o texto serão inseridos.
doc = fitz.open("modelo_contrato.pdf")  

# A seguir, criamos uma função chamada `add_image_to_page`. 
# Esta função adiciona uma imagem a uma página específica do PDF.
# Ela recebe como parâmetros:
# - `doc`: O documento PDF aberto.
# - `page_num`: O número da página onde a imagem será inserida.
# - `image_path`: O caminho da imagem que será inserida.
# - `x` e `y`: As coordenadas de onde a imagem será posicionada na página.
# - `width` e `height`: As dimensões da imagem.
def add_image_to_page(doc, page_num, image_path, x, y, width, height):
    page = doc[page_num]  # Acessa a página específica do PDF
    img = fitz.Pixmap(image_path)  # Carrega a imagem como um Pixmap
    rect = fitz.Rect(x, y, x + width, y + height)  # Define a área onde a imagem será inserida
    page.insert_image(rect, pixmap=img)  # Insere a imagem na área definida

# Agora, inserimos a rubrica (imagem) nas páginas 0 e 1 do PDF. 
# A imagem `rubrica.png` será posicionada nas coordenadas (50, 700) com 100x50 de tamanho.
rubrica_path = "rubrica.png" 
add_image_to_page(doc, 0, rubrica_path, 50, 700, 100, 50)
add_image_to_page(doc, 1, rubrica_path, 50, 700, 100, 50)

# Depois, inserimos a assinatura (imagem) na página 2 do PDF.
# A assinatura será posicionada nas coordenadas (100, 125), também com 100x50 de tamanho.
assinatura_path = "assinatura.png"  
add_image_to_page(doc, 2, assinatura_path, 100, 125, 100, 50)

# Na página 2, também inserimos a data atual logo acima da assinatura.
# Para isso, usamos a função `insert_text` que posiciona o texto nas coordenadas (105, 115).
# A data é obtida com `datetime.datetime.now().strftime("%d/%m/%Y")` para seguir o formato DD/MM/AAAA.
page3 = doc[2]
date_str = datetime.datetime.now().strftime("%d/%m/%Y")
page3.insert_text((105, 115), date_str, fontsize=12, color=(0, 0, 0))  # Insere a data em preto

# Por fim, salvamos o documento modificado com o nome "contrato_assinado.pdf" e fechamos o arquivo.
doc.save("contrato_assinado.pdf")
doc.close()

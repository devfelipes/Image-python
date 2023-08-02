import os
from PIL import Image
import piexif


def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('JPG') or nome_arquivo.endswith('PNG') or nome_arquivo.endswith('jpg') or nome_arquivo.endswith('heic'):
        return True
    return False

def reduzir_foto(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        try:
            exif_dict = piexif.load(imagem.info['exif'])
            orientacao = exif_dict['0th'][piexif.ImageIFD.Orientation]
        except:
            orientacao = 1

        if orientacao == 3:
            imagem = imagem.rotate(180, expand=True)
        elif orientacao == 6:
            imagem = imagem.rotate(-90, expand=True)
        elif orientacao == 8:
            imagem = imagem.rotate(90, expand=True)

        largura, altura = imagem.size
        proporcao = float(3840) / max(largura, altura)
        nova_largura = int(largura * proporcao)
        nova_altura = int(altura * proporcao)
        imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.LANCZOS)
        nome_sem_ext = os.path.splitext(nome)[0]
        imagem_redimensionada.save(os.path.join(output_dir, nome_sem_ext + ext), quality=20)



def criar_tumbnail(input_dir, output_dir, ext='.jpg'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        tamanho = (290,290)
        imagem.thumbnail(tamanho)      
        nome_sem_ext = os.path.splitext(nome)[0]
        imagem.save(os.path.join(output_dir, nome_sem_ext + ext), quality=40)



def play():
    diretorio = 'fotos'
    output = 'output'
    output_thumbnail = 'output\\thumbnail'
    reduzir_foto(diretorio, output)
    print('Todas as fotos foram reduzidas')
    criar_tumbnail(diretorio, output_thumbnail,  ext='.jpg')


play()
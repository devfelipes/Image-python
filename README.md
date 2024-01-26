# Script de Processamento de Imagens

Este script em Python foi projetado para processar imagens dentro de um diretório especificado. Ele oferece funcionalidades para redimensionar imagens e criar miniaturas mantendo as proporções e considerando as orientações das imagens.

## Funções

### `eh_imagem(nome_arquivo)`

- **Descrição**: Verifica se um arquivo possui uma extensão de imagem.
- **Parâmetros**:
  - `nome_arquivo`: Nome do arquivo.
- **Retorna**: 
  - `True` se o arquivo tiver uma extensão de imagem, caso contrário `False`.

### `reduzir_foto(input_dir, output_dir, ext='.jpg')`

- **Descrição**: Redimensiona imagens dentro do diretório de entrada especificado e as salva no diretório de saída.
- **Parâmetros**:
  - `input_dir`: Caminho para o diretório que contém as imagens originais.
  - `output_dir`: Caminho para o diretório onde as imagens redimensionadas serão salvas.
  - `ext`: Extensão para as imagens de saída (o padrão é '.jpg').
- **Processo**:
  1. Recupera uma lista de arquivos de imagem do diretório de entrada.
  2. Itera através de cada arquivo de imagem, abre-o e ajusta a orientação, se necessário.
  3. Redimensiona a imagem mantendo a proporção para se ajustar a uma largura máxima de 3840 pixels.
  4. Salva a imagem redimensionada no diretório de saída com qualidade reduzida.

### `criar_tumbnail(input_dir, output_dir, ext='.jpg')`

- **Descrição**: Cria miniaturas das imagens dentro do diretório de entrada especificado e as salva no diretório de saída.
- **Parâmetros**:
  - `input_dir`: Caminho para o diretório que contém as imagens originais.
  - `output_dir`: Caminho para o diretório onde as miniaturas serão salvas.
  - `ext`: Extensão para as miniaturas de saída (o padrão é '.jpg').
- **Processo**:
  1. Verifica se o diretório de saída existe; caso contrário, o cria.
  2. Recupera uma lista de arquivos de imagem do diretório de entrada.
  3. Itera através de cada arquivo de imagem, abre-o e cria uma miniatura com tamanho fixo de 290x290 pixels.
  4. Salva a miniatura no diretório de saída com qualidade reduzida.

### `play()`

- **Descrição**: Orquestra as operações de processamento de imagens.
- **Processo**:
  1. Especifica o diretório de entrada e os diretórios de saída para imagens redimensionadas e miniaturas.
  2. Chama `reduzir_foto()` para redimensionar imagens.
  3. Imprime uma mensagem indicando a conclusão do redimensionamento das imagens.
  4. Chama `criar_tumbnail()` para criar miniaturas.

## Uso

1. Certifique-se de que você tenha o Python instalado no seu sistema.
2. Instale as dependências necessárias usando `pip install Pillow piexif`.
3. Coloque suas imagens no diretório de entrada especificado.
4. Execute o script e ele processará as imagens conforme as funções definidas.

## Observação

- O script suporta imagens com as extensões: 'png', 'jpg', 'JPG', 'PNG' e 'heic'.
- Ele utiliza a biblioteca Python Imaging Library (PIL) e a biblioteca piexif para o processamento de imagens e manipulação de dados EXIF.
- Ajustes para as orientações das imagens são feitos com base nos metadados EXIF, quando disponíveis.

Sinta-se à vontade para modificar o script de acordo com seus requisitos específicos ou integrá-lo aos seus projetos.

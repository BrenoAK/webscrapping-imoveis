Este repositório contém um script Python que utiliza a biblioteca BeautifulSoup para extrair dados de imóveis de sites imobiliários.

Funcionalidades:

Extração de dados de imóveis, como:
Título
Descrição
Área
Quartos
Banheiros
Valor
Localização
Gravação dos dados extraídos em um arquivo CSV

o site original foi removido por licensas proprias, mas a base de scrapping é a mesma

Requisitos:

Python 3.6 ou superior
BeautifulSoup4
Pandas
Instalação:

Clone este repositório:
git clone https://github.com/BrenoAK/webscrapping-imoveis.git
Instale as dependências:
pip install -r requirements.txt
Uso:

Execute o script com o seguinte comando:
python webscrapping_imoveis.py -u <URL do site>
O script irá gerar um arquivo CSV chamado imoveis.csv na pasta atual.
Exemplo de uso:

python webscrapping_imoveis.py -u https://www.exemplo.com.br/imoveis
Saída:

O arquivo CSV gerado terá a seguinte formatação:

titulo,descricao,area,quartos,banheiros,valor,localizacao
...
Contribuições:

A comunidade é bem-vinda para contribuir com o projeto. Você pode reportar bugs, sugerir melhorias ou enviar pull requests.

Licença:

Este projeto está licenciado sob a licença MIT.

Contato:

BrenoAK - breno.ak@email.com

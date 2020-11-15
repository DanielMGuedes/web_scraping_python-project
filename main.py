## WEB SCRAPING 
#  Deve-se ter cuidado ao utilizar essa técnica para não ser considerado uma prática maliciosa
# Ver sempre sobre a permissão de uso
#  é uma técnica para coletar dados de sites
# Uso da biblioteca BeautifulSoup

# Para iniciar o projeto é necessário instalar as dependências do projeto 
# para isso, dentro da pasta do projeto, no terminal utilizamos os comandos:
# "pip install requests"  e  "pip install beatifulsoup4"



import requests
from bs4 import BeautifulSoup

#Criando variavel que vai receber o conteudo do site apontado. Também já configuramos o encoding para UTF-8
res = requests.get("https://digitalinnovation.one/blog/")
res.encoding = 'utf-8'
print(res)
# Neste momento sugiro fazer um teste com o terminal utilizando chamando o arquivo: "python main.py" 
# Se o resultado for "Response [200]" significa que a concexão foi estabelecida. Se o resulta for diferente
# aconteceu erro na conexão que pode ser por causa das autorizações do site.


# PAra Trazer todo o conteudo da pagina, vamos criar outa variavel e dar um "soup" para que o html leia toda a # # #pagina como objetos

#soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# Apartir da variavél SOUP vamos fazer o scraping 
#posts = soup.find_all(class_="posts")
				

# Deve-se executar o arquivo no terminal para ver se está funcionando.
# O Próximo passo é colocar a variavel "all_books" em um Dicionário para depois transformar em JSON
'''
all_posts = []
for post in posts:
    info = post.find(class_='post-content')
    title = info.h2.text
    preview = info.p.text
    author = info.find(class_= "post-author").text'''

        
    #print(book.find('h2').text
    





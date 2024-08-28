import re

text = '''100. williamcepeda@Williams-MacBook-Pro VSProjects % py
/Users/williamcepeda0/objectel/GitAll/VSProjects/.venv/bin/python
 /Users/williamcepedab1342/objectel/GitAll/VSProjects/excepciones/mi_excepcion.py
Clase Mi    excepcion error \n--> Try la excepcion ab22.  Except section except3.'''

resultado = re.findall('VSProjects',text)

# busca numeros
resultado = re.findall(r"\d",text)

#todo menos los numeros
resultado = re.findall(r"\D",text)

#\w busca [a-zA-z0-9_]
resultado = re.findall(r"\w",text)

#\W todo menos los alfanumericos
resultado = re.findall(r"\W",text)

# \s espacios en blanco, tab, salto de linea ..
resultado = re.findall(r"\s",text, flags=re.M)

# \S
resultado = re.findall(r"\S",text)

#\. except saltos de linea
resultado = re.findall(r".",text)

# \n saltos de linea
resultado = re.findall(r"\n",text)

# \ no caracteres especiales
resultado = re.findall(r"\.",text)

# busque numero punto espacio
resultado = re.findall(r"\d\.\s",text)

# busca inicio de linea
resultado = re.findall(r"^Clas|^100",text, flags=re.M)

resultado = re.findall(r"3.$|^100",text, flags=re.M)

# digitos contiguos
resultado = re.findall(r"\d{3}",text )

resultado = re.findall(r"\d{2,4}\.|\d{2,3}",text)
resultado = re.findall(r"(ab)\d{2,4}",text)

# busuqe lo que inicie con 100 no tenga salto de linea y linea termine en py
text = "100 \.williamcepeda@Williams-MacBook-Pro VSProjects % py"
x = re.search("^100.*py$",text)


if x:
    print('SI')
else:
    print('No')

text = "100. williamcepeda@Williams-MacBook-Pro 01/01/2024 VSProjects % py"

pattern = r"\d{2}/\d{2}/\d{4}"

replacement = '\n2024-08-27\n'
new_text = re.sub(pattern, replacement, text)
new_text = re.sub("[aeiuo]","*",text)

email = "william-cepeda@Williams-MacBook-Pro.com"
pattern = "[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

x= re.match(pattern,email)

if x:
    print(f'email: {email}    bien formado')
else:
    print('email incorrecto')


text = "mi sitio web https://www.objectel.com existe y opera"
pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
resultado = re.findall(pattern, text)

text = "Mi numero +1 949 267-8526 personal"
pattern =r"\+\d{1,3}\s\d{3}\s\d{3}-\d{4}"
resultado = re.sub(pattern, "**********", text)


print(resultado)

#print(new_text)
#print(email)
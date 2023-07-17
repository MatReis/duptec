# Etapas pra rodar o projeto

criar ambiente de desenvolvimento

``` python
    python -m venv .venv
```

ativar ambiente no windows

``` shell
    .\.venv\Scripts\Activate.ps1
```

baixar dependências do projeto

``` python
    pip install -r requirements.txt
```

# banco de dados

precisa ter o docker instalado

crie a imagem do mysql
``` shell
    docker build -t mysql-image .
```

para criar o container
 ```shell
    docker run --name mysql-container -p 3306:3306 -d mysql-image
 ```

 # rodar o jupyter

 ``` shell
 jupyter-lab
 ```
# Diário de estudos 

## Configuração ambiente

- ### Pylint

    - Instalação:
        - pip3 install pylint

    - Criando arquivo de configuração:
        - pylint --generate-rcfile > .pylintrc
        - obs.: configurar essa parte como preferir

        - Códigos adicionados para o pylint, não validar durante o processo de commit:
        
        >
            disable=
                C0114, # Missing-module-docstring
                C0115, # Missing-class-docstring
                C0116, # Missing-function-docstring
                C0321, # multiple-statements
                W0703, # Catching too general exception Exception
                W0719, # broad-exception-raised
                C0209, # Consider-using-f-string
                C0301, # Line too long
                C0303, # Trailing whitespace
                E0015, # unrecognized-option
                R0903, # Too few public methods

- ### Pre-commit

    - Instalação:
        - pip3 install pre-commit

    - Inicializando:
        - pre-commit install
        - obs.: Executar dentro da pasta raiz do projeto

    - Criar na raiz do projeto:
        - arquivo .pre-commit-config.yaml
        - adicionar as seguintes informações no arquivo:

        >
            repos:
                - repo: local
                    hooks:
                    - id: pylint
                        name: pylint
                        entry: pylint
                        language: system
                        types: [python]
                        args:
                        [
                            "-rn", # Only display messages
                            "-sn", # Don't display the score
                            "--rcfile=.pylintrc", # Link to your config file
                            "--load-plugins=pylint.extensions.docparams", # Load an extension
                        ]

## [Padrões de commits](https://github.com/iuricode/padroes-de-commits)
-
- A título de curiosidade e organização, o commit semântico possui os elementos estruturais abaixo (tipos), que informam a intenção do seu commit ao utilizador(a) de seu código.

    - feat- Commits do tipo feat indicam que seu trecho de código está incluindo um novo recurso (se relaciona com o MINOR do versionamento semântico).

    - fix - Commits do tipo fix indicam que seu trecho de código commitado está solucionando um problema (bug fix), (se relaciona com o PATCH do versionamento semântico).

    - docs - Commits do tipo docs indicam que houveram mudanças na documentação, como por exemplo no Readme do seu repositório. (Não inclui alterações em código).

    - test - Commits do tipo test são utilizados quando são realizadas alterações em testes, seja criando, alterando ou excluindo testes unitários. (Não inclui alterações em código)

    - build - Commits do tipo build são utilizados quando são realizadas modificações em arquivos de build e dependências.

    - perf - Commits do tipo perf servem para identificar quaisquer alterações de código que estejam relacionadas a performance.

    - style - Commits do tipo style indicam que houveram alterações referentes a formatações de código, semicolons, trailing spaces, lint... (Não inclui alterações em código).

    - refactor - Commits do tipo refactor referem-se a mudanças devido a refatorações que não alterem sua funcionalidade, como por exemplo, uma alteração no formato como é processada determinada parte da tela, mas que manteve a mesma funcionalidade, ou melhorias de performance devido a um code review.

    - chore - Commits do tipo chore indicam atualizações de tarefas de build, configurações de administrador, pacotes... como por exemplo adicionar um pacote no gitignore. (Não inclui alterações em código)

    - ci - Commits do tipo ci indicam mudanças relacionadas a integração contínua (continuous integration).

    - raw - Commits do tipo raw indicam mudanças relacionadas a arquivos de configurações, dados, features, parâmetros.

    - cleanup - Commits do tipo cleanup são utilizados para remover código comentado, trechos desnecessários ou qualquer outra forma de limpeza do código-fonte, visando aprimorar sua legibilidade e manutenibilidade.

    - remove - Commits do tipo remove indicam a exclusão de arquivos, diretórios ou funcionalidades obsoletas ou não utilizadas, reduzindo o tamanho e a complexidade do projeto e mantendo-o mais organizado.

## Ordem das Operações no Python

- A ordem das operações em python, seguem a mesma ordem e a mesma lógica da matemática mesmo.
- Por exemplo:
    - print(1 + 2 * 2), resultaria em 5, pois, seria resolvido primeiro a multiplicação para depois a soma.
    - se caso, fosse necessário realizar a soma antes, seria preciso colocar um parênteses envolvendo a soma, como da seguinte forma:
        - print((1+2) * 2)

## Tipos de Varíaveis em Python
- Qualquer coisa em python pode ser uma varíavel
- As varíaveis são objetos
    - Varíaveis de tipos diferentes, vão ter métodos diferentes.
- Não pode ou não é recomendado ficar mudando o tipo da varíavel o tempo todo

## Métodos de String
 - Método é uma fórmula/ação que é feito em determinado texto.
 - Todos os métodos do python, funcionam no formato texto.método()

 ### capitalize()
 - Coloca a 1˚ letra maiúscula
    >
        texto = 'brunno'
        print(texto.capitalize())

        Resultado: 'Brunno'

### casefold()
- Transforma todas as letras em minúsculas(existe lower(), mas o casefold é melhor normalmente)

    >
        texto = 'Brunno'
        print(texto.casefold())

        Resultado: 'brunno'

### count()
- Quantidade de vezes que um valor aparece na string

    >
        texto = 'brunnomanducarfe@gmail.com'
        print(texto.count('.'))

        Resultado: 1

### endswith()
- Verifica se o texto termina com um valor especifico e da como resposta True ou False

    >
        texto = 'brunnomanducarfe@gmail.com'
        print(texto.endswith('gmail.com'))

        Resultado: True

### find()
- Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado.

    >
        texto = 'brunnomanducarfe@gmail.com'
        print(text.find('@'))

        Resultado: 16

        Obs.: lembrando de como funciona a posição nas strings, então o @ está na posição 16
        b r u n n o m a n d  u  c  a  r  f  e  @  g  m  a  i  l  .  c  o  m
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25


### format()
- Formata uma string de acordo com os valores passados.

    >
        faturamento = 1000
        print('O faturamento da loja foi de {} reais'.format(faturamento))

        Resultado: 'O faturamento da loja foi de 1000 reais'

### isalnum()
- Verifica se o texto é todo feito com caracteres alfanúmericos (letras e números) -> letra 
com acento e ç são considerados letras para essa função.

    >
        texto = 'João123'
        print(texto.isalnum())

        Resultado: True

        Obs.: Se o texto fosse 'Jo~ao' ou então 'Joao#' o resultado seria False

### isalpha()
- Verifica se um texto é todo feito de letras

    >
        texto = 'Brunno'
        print(texto.isalpha())

        Resultado: True

        Obs.: nesse caso se o texto fosse 'Joao123' o resultado seria False, porque 123
        não são letras

### isnumeric() -> Verifica se um texto é todo feito por números

    texto = '123'
    print(texto.isnumeric())

    Resultado: True

    Obs.: Existem os métodos isdigit() e isdecimal() que tem variações pontuais em caracteres
    especiais tipo textos com potências, mas para 99% dos casos eles não vão ser necessários.


### replace() -> Substitui um texto por outro texto em uma string.

    >
        texto = '1000.00'
        print(texto.replace('.',','))

        Resultado: '1000,00'

        Obs.: O replace precisa de 2 argumentos para funcionar. O 1˚ é o texto que você quer
        trocar. O 2˚ ;e o texto que você quer colocar no lugar daquele texto que você está
        tirando.

### split() -> Separa uma string de acordo com um delimitador em vários textos diferentes

    >
        texto = 'brunnomanducarfe@gmail.com'
        print(texto.split('@'))

        Resultado: ['brunnomanducarfe', 'gmail.com']

### splitlines() -> separa um texto em vários textos de acordo com os 'enters' do texto

    >
        texto = ''Olá, bom dia
        Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
        Faturamento = R$2.500,00
        ''''

        print(texto.splitlines())

        Resultado = ['Olá, bom dia', 'Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.', 'Faturamento = R$2.500,00']

### startswith() -> Verifica se a string começa com um determinado texto

    >
        texto = 'BEB123456'
        print(texto.startswith('BEB'))

        Resultado: True

### strip() -> Retira caracteres indesejados dos textos. Por padrão, retira espaços extras no ínicio e no final

    >
        texto = ' BEB123456 '
        print(texto.strip())

        Resultado: 'BEB123456'

### title() -> Coloca a 1˚ letra de cada palavra em maiúscula

    >
        texto = 'brunno manduca do prado'
        print(text.title())

        Resultado = 'Brunno Manduca do Prado'

### upper() -> Coloca o texto todo em letra maiúscula

    >
        texto = 'beb1234'
        print(texto.upper())

        Resultado = 'BEB1234'


## Listas em Python
- são mutáveis.

### Estrutura:
- lista = [valor, valor, valor, ....]

    - Lista é um dos objetos mais importantes de Python
    - Quando importamos uma base de dados para o Python, normalmente ela é lida como uma 'lista' ou como alguma 'variação de lista'
    - Lista em Python foram feitas para serem homogêneas, apesar de aceitarem valores heterogêneos

### Juntando listas
- Para juntar duas listas existem duas forma de fazer esse processo:
    1. Método extend()
        - No método extend você vai estar editando a sua lista original
    2. Somando as duas listas
        - Normalmente quando é somado duas listas, vai ser criado uma nova lista para isso.

## Strings em Python
- Todas as strings por debaixo dos panos são consideradas listas de caracteres, porém, a única diferença para uma lista mesmo, é que as strings não são mutáveis, ou seja, não podem ser alteradas.

    >
        email = brunnomanducarfe@gmail.com
        # incorreto
        email[5] = 'a'
        # correto
        email = email.replace('o', 'a')
        print(email)

        Resposta: brunnamanducarfe@gmail.cam

## Enumerate
- O enumerate permite que você percorra uma lista e ao mesmo tempo tenha em uma variável o índice daquele item.

    >
        for i, item in enumerate(lista):
            restante do codigo...


## While

- O uso do while se define em repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa
- A lógica é: enquanto a condição for verdadeira, o while executa o código. Assim que ele terminar de ser verdadeira, o código 'sai' do while.

    >
        while condicao:
            repete o codigo

## Tuplas
- estrutura: tupla = (valor, valor, valor, ...)
- Diferença: parece uma lista mas é imutável.
- Vantagens:
    1. Mais eficiente (em termos de performance)
    2. Protege a base de dados (por ser imutável)
    3. Muito usado para dados heterogêneos

- unpacking: 
    - ação de desmembrar os itens de uma tupla
    - podemos fazer da seguinte forma:
        >
            vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')

            nome, data_contratacao, data_nascimento, salario, cargo = vendas

- enumerate:
    - Cria uma tupla, da sguinte forma:
        >
            for i, venda in enumerate(vendas):
                print(f'{funcionarios[i]} vendeu {venda} unidades')


## Dicionários

- Estrutura

    >
        dicionario = {chave: valor, chave: valor, chave: valor, chave: valor, ...}


- **Vantagens e desvantagens**
    1. Não devem ser usados para pegar itens em uma determinada ordem
    2. Podem ter valores heterogêneos (vários tipos de valores dentro de um mesmo dicionário: inteiros, strings, listas, etc.)
    3. Chaves são únicas obrigatoriamente
    4. Mais intuitivos de trabalhar.

- **Método keys()**
    - 'Pega' todas as chaves do dicionário
    - porém ao aplicar o método keys, nos criamos uma dict_keys
    - para 'transformar' o resultado em uma lista realmente:
        - isto serve tanto para o método keys quanto para o values
        >
            lista_chaves = list(dicionario.keys())

- **Método values()**
    - 'Pega' todos os valores do dicionário
    - porém ao aplicar o método values, nos criamos uma dict_values


## Iterables
- O que é?
    - Explicação não programadora: Um iterable é uma estrutura que armazena dados que podem ser 'iterada', ou seja, que você pode fazer um loop com um for dentro dela e ir passando de item a item. É como se fosse um tipo de lista de coisas que você pode ir olhando cada um dos elementos dentro dela.

## Set
- Basicamente é uma lista de informações, em que essas informações não tem uma ordem definida, ou seja, elas podem vir em qualquer ordem.
- Vantagem: Não pode ter valores duplicados
    >
        meu_set = {valor, valor, valor, ....}

## Functions
- As functions são blocos de código que servem para um 1 único propósito: fazer uma ação específica.

- Estrutura básica
    >
        def nome_funcao():
            faca alguma coisa
            faca outra coisa
            return valor_final

- Formas de passar um argumento para uma function:
    1. Em ordem -> positional argument
        >
            def program(arg1, arg2):
                seu codigo...

            program(cor1, cor2)
        
        - desta forma, o arg1 automaticamente será a cor1 e o arg2 será a cor2
    
    2. Com o nome do argumento (keyword argument)
        >
            def verificar_categoria(bebida, cod_categoria):
                bebida = bebida.upper()
                if cod_categoria in bebida:
                    return True
                else:
                    return False

            produtos = ['CAR46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

            for produto in produtos:
                if verificar_categoria(cod_categoria = 'BEB', bebida = produto):
                    print('Enviar {} para setor de bebidas alcóolicas'.format(produto))
                elif verificar_categoria(produto, 'BSA'):
                    print('Enviar {} para setor de bebidas não alcóolicas'.format(produto))

## Docstrings e Annotations
- Quando criamos uma função, normalmente não seremos as únicas pessoas a usarem essa função e também pode ser que a gente precise usar a mesma função semanas, meses ou até anos depois da sua criação.
- Por isso é importante usarmos DOcStrings e Annotations:
    1. Docstring: Diz o que a função faz, quais os valores ela tem como argumento e o que significa cada valor.
    2. Annotation: Diz o que devem ser os argumentos e o que a função retorna.
- Em muitas empresas, o time de tecnologia vat ter um padrão que você deve seguir para isso, caso não tenha, abaixo tem um padrão que pode ser utilizado

- ### Docstring
    >
        def minha_soma(num1, num2, num3):
            ''' 
                Faz a soma de 3 número inteiros e devolve como resposa um número inteiro

                Parameters:
                    num1 (int): primeiro número a ser somado
                    num2 (int): segundo número a ser somado
                    num3 (int): terceiro número a ser somado

                Returns:
                    soma (int): o valor da soma dos 3 números dados como argumento.
            '''

            return num1 + num2 + num3

- ### Annotation
    >
        def minha_soma(num1: int, num2: int, num3: int) -> int:
            return num1 + num2 + num3

## Quantidade indefinida de argumentos
- Utilidade: quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso
- Estrutura:
    >
        # *args para positional arguments -> argumentos que vêm em formato de tupla
        def minha_soma(*numeros):
            print(numeros)
            soma = 0
            for numero in numeros:
                soma += numero
            return soma

    >
        # **kwargs para keywords arguments -> argumentos que vem em formato de dicionário
        def minha_funcao(**kwargs):
            ...


## Ordem de argumentos
- Estrutura:
    1. Sempre os positional arguments vêm antes e depois os keywords arguments
    2. Sempre os argumentos individuais vem antes e depois os múltiplos

    >
        def minha_funcao(arg1, arg2, arg3, *args, k = kwarg1, k2 = kwarg2, k3 = kwarg3, **kwargs)
            ...

## List Comprehensions
- É uma forma de iterar pelos elementos das listas de uma maneira 'mais direta', com mais 'cara de Python'
- Em resumo: É como se você fizesse um for em uma linha de código.

- ### Observação importante
    - Você não precisa de List comprehension para programar, todos os problemas resolvidos através do uso de List comprehension pode ser realizado com as outras formas já aprendidas no python
    - Não será possível sair de uma hora para outra fazendo tudo de list comprehension ao invés de for, porque realmente é mais confuso
    - O objetivo qual é:
        1. Saber ler e entender o que está acontecendo quando ver list comprehension(principal)
        2. A medida do tempo que você vai se acostumando com isso, vendo mais, usando mais e vai fazer naturalmente quando precisar.
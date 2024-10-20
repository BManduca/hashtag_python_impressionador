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
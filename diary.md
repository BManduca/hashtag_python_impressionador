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


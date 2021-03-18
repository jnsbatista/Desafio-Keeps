# Desafio Desenvolvimento Keeps

Esse desafio tem como objetivo avaliar as habilidades necessárias de um desenvolvedor front-end, 
visando atender os requisitos da stack da Keeps.


## O Desafio

O candidato deverá criar uma aplicação WEB que irá permitir gerir uma 'mini' solução de e-learning, que
terá cursos, alunos e matrículas.

Esse teste será dividido em fases de dificuldades. Não são obrigatórias todas as etapas, o candidato 
será avaliado pelas quais foram concluídas, sendo que, quanto mais longe o candidato avançar no desafio, 
teremos mais condições de avaliar e melhor será sua pontuação.


Etapas:
1) Configurar seu ambiente
2) Desenvolver a aplicação básica.
3) Criar testes de integração com POSTMAN
4) Criação de testes unitários.
5) Refatorar o código, utilizando NGRX
6) Autenticar a aplicação utilizando o IAM Keycloak.

### 1) Configurando o seu ambiente

Esse projeto tem um servidor de aplicações desenvolvido em Python + Django que será rodado localmente para 
facilitar a consumo de uma API. Não é necessário entender de Python e nem configurar banco de dados, um SQLITE
será criado ao rodar a aplicação.

Para essa etapa o candidato deverá:
- Fazer um fork desse projeto, criando um repositório na sua própria conta (caso não tenha, criar uma conta do Gitlab, é gratuito.)
- Instalar o Python 3.6+ na sua máquina caso não esteja instalado;
- Rodar a aplicação utilizando um dos script (conforme o seu SO):
  
Scripts por SO:

        run-mac.sh
        run-linux.sh
        run-win.bat

Ao rodar a aplicação, o servidor estará respondendo na porta 8000, basta acessar:

    http://localhost:8000

O acesso à documentação da API será pelo endereço:

    http://localhost:8000/docs

*O que será avaliado*
- Capacidade de montar um ambiente de desenvolvimento.
- Conhecimento em GIT

### 2) Desenvolvimento da Aplicação Web

Desenvolver uma aplicação WEB para que o gestor da área de treinamento de uma empresa/escola possa criar e
administrar cursos, alunos e matrículas. A aplicação deverá ter que cumprir os seguintes requisitos:

- Deve permitir gerenciar as categorias para os cursos;
- Deve permitir cadastrar um curso;
- Deve permitir editar os dados do curso;
- Deve permitir excluir um curso;
- Deve permitir cadastrar um estudante;
- Deve permitir editar os dados do estudante;
- Deve permitir excluir um estudante;
- Deve permitir matricular um estudante em um curso;
- Deve permitir cancelar uma matrícula de um estudante em um curso;
- Criar uma listagem de cursos;
- Criar uma listagem de alunos;
- Criar uma listagem de matrículas;
- Utilizar pop-ups de confirmações em ações;
- Tratamento dos erros (apresentar para o usuário);

Toda a documentação da APIs e a modelagem dos dados se encontra no servidor:
    
    http://localhost:8000/docs 

Dentro da pasta **assets** encontra-se alguns modelos de telas. São sugestões de como poderia ficar sua
aplicação dentro deste contexto, mas sinta-se livre para criar outras possibilidades, um dos itens da
avaliação também é o conhecimento de UX/UI. Todos os componentes dos protótipos (cards, tabelas, pop-ups, ...)
estão disponíveis na biblioteca do **Material Design**, não é necessário criar componentes.


*Utilizar:*
- Angular versão acima da 10
- Material Design / Angular Material
- SaaS

*O que será avaliado:*
- Conhecimento de Angular
- Conhecimento de HTML e CSS
- Conhecimento de Material Design
- Conhecimento em comunicação com a API REST
- Noções básicas de UX/UI
- Qualidade de código (padrões da linguagem)


### 3) Criar testes de integração com POSTMAN

Desenvolver aplicações WEB SPA exige conhecimento do protocolo REST e entendimento da documentação de uma API. 
E no desenvolvimento dessas soluções, uma das ferramentas utilizadas para testar as APIs e criar fluxos 
automatizados de testes é o POSTMAN.

Download e acesso:

    https://www.postman.com/

Tutorial para criar testes:

    https://medium.com/assertqualityassurance/automatizando-sua-api-com-postman-64a72185e1e6

*O que será avaliado*
- Conhecimento do POSTMAN;
- Se não conhecer o POSTMAN, capacidade de aprendizagem;
- Compreensão da API;
- Capacidade de entender quais são os fluxos de um sistema e testa-los;


### 4) Criação de testes unitários
    
Outro ponto importante no desenvolvimento de aplicações WEB são os testes. Nesse item queremos avaliar se
o candidato tem conhecimento com ferramentas de testes e consegue ter uma compreensão ampla do contexto.

*O que será avaliado*
- Noções básicas de testes


### 5) Refatorar o código, utilizando NGRX

O NGRX é um padrão de programação REATIVA e adotado pela Keeps para organizar a nossa solução.

Nesse item, o candidato deverá refatorar o que foi feito no item 2 para utilizar
os conceitos do NGRX.

Documentação:

    https://ngrx.io/

Tutorial básico:

    https://movile.blog/construindo-aplicacoes-front-end-reativas-com-ngrx/


## 6) Autenticar a aplicação utilizando o IAM Keycloak.

Para autenticar nas nossas aplicações, utilizamos o Keycloak, que implementa o protocolo OAuth para
autorizar o acesso.

Para ativar a autenticação na API, você deverá configurar uma variável de ambiente e rodar o servidor novamente.

Cada sistema operacional tem sua forma de configurar uma variável de ambiente, segue um exemplo de como fazer
em sistemas UNIX

    export ENABLE_AUTH=TRUE

Você deve pagar o servidor, criar a variável ENABLE_AUTH e depois rodar novamente. Ao tentaar fazer uma
nova chamada na API, você receberá um erro dizendo que precisa de um token de autenticação.

Na aplicação WEB, será necessário utilizar o biblioteca *keycloak.js*.

    https://www.npmjs.com/package/keycloak-js

Ao chegar nesse item, será necessário obter algumas chaves de integração. Para que essa chaves não fiquem
expostas no documento, ao chegar nessa etapa solicitar essas informações para alguém responsável da Keeps.

*O que será avaliado*
- Conhecimento em como autenticar uma aplicação;
- Funcionamento do protocolo OAuth
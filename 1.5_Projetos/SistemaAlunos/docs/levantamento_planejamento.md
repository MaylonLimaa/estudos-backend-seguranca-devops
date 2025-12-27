# 1 - Levantamento de Requisitos
Trata-se de um sistema de alunos utilando um **CRUD** básico.

## Ferramentas
- Módulo datetime
- diagrams.net (draw.io) – Criação de diagramas UML

## Funcionalidades do Sistema
### Cadastrar Aluno
- O sistema deve cadastrar um aluno. Com nome, ano de nascimento e notas. 
Aluno deve ter mais de 5 anos e menos de 18. Notas devem estar entre 0 e 10.
- Caso o aluno exista, o sistema deve avisar.

### Atualizar Aluno
- Atualizar dados do aluno. Atualizando notas, devemos atualizar média e situação.
- Caso o aluno não exista, o sistema deve avisar.

### Consulta de Aluno
- Mostra dados de um aluno. Nome, idade, notas, média e a situação(média maior que 7 aprovado)

### Listar Alunos
- Mostra todos os alunos. Nome, idade e média.

### Excluir Aluno
- Exclui totalmente um aluno.
- Adiciona ele na lista de alunos excluidos

# 2 – Planejamento

**Nesta etapa foi definido o planejamento de como o sistema irá funcionar, estabelecendo quais elementos serão classes, métodos, atributos, objetos, variáveis e funções.**

## Classes
Neste tópico vou abordar sobre quais classes vão ser criadas no projeto e o porque, também será verificado suas caracteristicas e comportamentos.

## Aluno
A classe aluno é a principal e única classe do projeto, pois, pelas funcionalidades do projeto, não há necessidade de outras classes.
### Atributos
- nome
- nascimento
- idade
- notas
- media
- situacao_media
- situacao_cadastro

### Métodos
- Construtor
O método construtor vai definir os atributos de instanciamento, ou seja, oque cada objeto precisa ter individualmente.
TODOS os atributos serão instanciados dentro do construtor, porém os atributos que receberão valores direto são:
- nome
- nascimento
- notas
Estes três atributos serão obrigatoriamente devem ser passados como parametro do método.
- Método especial str
Este método vai ser usado para facilitar a exibição dos alunos.
- calc_idade()
O método calc_idade() vai receber como parametro nascimento e vai calcular a idade baseada nele.
Para isso vamos usar o módulo datetime do python.
- calc_media()
Recebe como parametro notas e, com isso, calcula a média.
- verifica_situ_media()
Recebe como parametro média e baseado nisso define a situação do aluno.
- atualizar_dados()
Este método recebe como parametro notas novas, baseado nestas notas recalcula média e situação.
Este método apenas vai atualizar notas, não sendo possível atualizar nome e nascimento de um aluno por questões de segurança.

Todas as outras funcionalidades do projeto serão controladas por funções, requisitadas através de um arquivo nomeado
"services.py"

## Services
Neste módulo será onde todas as funções de controle vão estar armazenadas e devidamente documentadas.
### Cadastrar
Está função será responsável por cadastrar um aluno, ela também valida se o aluno já existe.
Parte das validações serão atribuidas a Classe Aluno e outra parte será feita em nesta função.
### Atualizar
Essa função é responsável por atualizar as notas de um aluno, a média é alterada automáticamente sempre que as notas mudam, a alteração da média gera atualização da situação do aluno. Está função altera diretamente apenas notas e média, situação é alterada como consequência. Os outros dados, por segurança, não devem ser atualizados, caso seja necessário atualizar outro dado é necessário excluir um aluno e depois cadastrar com os dados corretos.
A função valida caso algum aluno exista ou não.
### Consultar
Está função é a responsável por verificar as informações de um único aluno. Será utilizado um ID para busca, pois, será possível ter nomes iguais neste exercicio. Ela busca também alunos excluidos.
A função valida caso algum aluno exista ou não.
### Listar
Função responsável por listar todos os alunos existentes.
Será possível selecionar se deseja ver os alunos excluidos, todos os alunos ou apenas os alunos ativos.
### Excluir
Função responsável por excluir um aluno, ela deve guardar os dados dos alunos excluidos para consulta se necessário.

## Linguagem escolhida
O sistema será desenvolvido em Python, por ser uma linguagem de alto nível,
com sintaxe simples, forte suporte à Programação Orientada a Objetos e
amplamente utilizada no desenvolvimento de sistemas de pequeno e médio porte.
Além disso, a escolha do Python está alinhada com o foco atual dos estudos,
permitindo maior aprofundamento na linguagem durante o desenvolvimento do projeto.

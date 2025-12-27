# 1 - Levantamento de Requisitos
Trata-se de um sistema de alunos utilizando um **CRUD** básico.

## Ferramentas
- Módulo `datetime`
- diagrams.net (draw.io) – Criação de diagramas UML

## Funcionalidades do Sistema
### Cadastrar Aluno
- O sistema deve cadastrar um aluno com nome, ano de nascimento e notas.
Aluno deve ter mais de 5 anos e menos de 18. Notas devem estar entre 0 e 10.
- Caso o aluno já exista, o sistema deve avisar.

### Atualizar Aluno
- Atualizar dados do aluno. Ao atualizar as notas, devemos atualizar também a média e a situação.
- Caso o aluno não exista, o sistema deve avisar.

### Consulta de Aluno
- Mostra os dados de um aluno. Nome, idade, notas, média e a situação (média maior ou igual a 7 aprovado).
- Também mostra se o aluno está ativo ou excluído.

### Listar Alunos
- Mostra todos os alunos. Nome, idade e média.

### Excluir Aluno
- Exclui totalmente um aluno.
- Adiciona o registro na lista de alunos excluídos.

# 2 – Planejamento

**Nesta etapa foi definido o planejamento de como o sistema irá funcionar, estabelecendo quais elementos serão classes, métodos, atributos, objetos, variáveis e funções.**

## Classes
Neste tópico, vou abordar quais classes serão criadas no projeto e o porquê; também serão verificadas suas características e comportamentos.

## Aluno
A classe aluno é a principal e única classe do projeto, pois, pelas funcionalidades previstas, não há necessidade de outras classes.

### Atributos
- **nome**
- **nascimento**
- **idade**
- **notas**
- **media**
- **situacao_media**
- **situacao_cadastro**

### Métodos
- **Construtor**
O método construtor vai definir os atributos de instanciamento, ou seja, o que cada objeto precisa ter individualmente. TODOS os atributos serão instanciados dentro do construtor, porém os atributos que receberão valores diretos são: nome, nascimento e notas. Estes três atributos obrigatoriamente devem ser passados como parâmetro do método.

- **Método especial str**
Este método vai ser usado para facilitar a exibição dos dados dos alunos.

- **calc_idade()**
O método `calc_idade()` vai receber como parâmetro o nascimento e vai calcular a idade baseada nele. Para isso, vamos usar o módulo `datetime` do Python.

- **calc_media()**
Recebe como parâmetro as notas e, com isso, calcula a média aritmética.

- **verifica_situ_media()**
Recebe como parâmetro a média e, baseado nisso, define a situação do aluno.

- **atualizar_dados()**
Este método recebe como parâmetro notas novas e, baseado nelas, recalcula a média e a situação. Este método apenas atualizará as notas, não sendo possível atualizar nome e nascimento de um aluno por questões de segurança.

Todas as outras funcionalidades do projeto serão controladas por funções, requisitadas através de um arquivo nomeado "services.py".

## Services
Neste módulo estarão armazenadas e devidamente documentadas todas as funções de controle.

### Cadastrar
Esta função será responsável por cadastrar um aluno; ela também valida se o aluno já existe. Parte das validações será atribuída à Classe Aluno e outra parte será feita nesta função.

### Atualizar
Essa função é responsável por atualizar as notas de um aluno; a média é alterada automaticamente sempre que as notas mudam, e a alteração da média gera a atualização da situação do aluno. Esta função altera diretamente apenas notas e média; a situação é alterada como consequência. Os outros dados, por segurança, não devem ser atualizados. Caso seja necessário atualizar outro dado, é necessário excluir o aluno e depois cadastrá-lo com os dados corretos. A função valida se o aluno existe ou não.

### Consultar
Esta função é a responsável por verificar as informações de um único aluno. Será utilizado um ID para busca, pois será possível ter nomes iguais neste exercício. Ela busca também alunos excluídos. A função valida se o aluno existe ou não.

### Listar
Função responsável por listar todos os alunos existentes. Será possível selecionar se deseja ver os alunos excluídos, todos os alunos ou apenas os alunos ativos.

### Excluir
Função responsável por excluir um aluno; ela deve guardar os dados dos alunos excluídos para consulta, se necessário.

## Linguagem escolhida
O sistema será desenvolvido em Python, por ser uma linguagem de alto nível, com sintaxe simples, forte suporte à Programação Orientada a Objetos e amplamente utilizada no desenvolvimento de sistemas de pequeno e médio porte. Além disso, a escolha do Python está alinhada com o foco atual dos estudos, permitindo maior aprofundamento na linguagem durante o desenvolvimento do projeto.

O banco de dados possui 3 tabelas principais(Aluno, Professor e Materia) e duas tabelas apenas para manter o relacionamento entre as entidades. A tabela Notas e ProfessorResponsável. As 3 tabelas principais são responsáveis por armazenar as informações do sistema como os Alunos, Professores e as matérias. Enquanto a tabela ProfessorResponsável armazena qual professor é responsável por cada matéria enquanto a tabela Notas armazena as notas dos alunos e a média.

Banco de dados
O banco de dados vai funcionar da seguinte forma.
Tabela Alunos armazena:
Matricula PK; nome texto; CPF valor inteiro unico; email texto; status texto;
Tabela Professor armazena:
Matricula PK; nome texto; CPF valor inteiro unico; email texto; status texto;
Tabela Materia armazena:
idmateria PK; nome texto;
Tabela ProfessorResponsável:
matriculaprofessor fk; idmateria fk;
Tabela Notas armazena;
matriculaaluno fk; idmateria fk; notas real;

A tabela Aluno armazena os principais dados de aluno, enquanto a tabela Notas armazena as notas do aluno de acordo com a matéria que ele cursa.
A tabela Professor armazena os principais dados de professor, enquantoa  tabela ProfessorResponsável armazena as matérias que ele é responsável.
A tabela Matéria armazena os dados da matéria.
Os dados relevantes vão ser guardados em um banco de dados, porém, dados como média e se o aluno está aprovado ou reprovado serão calculados de acordo com as notas, sendo aplicado um método para isso.


Aluno precisa ter:
nome, cpf, email, matricula, ativo, notas.
Professor precisa ter:
nome, cpf, email, matricula, ativo.
Materia precisa ter:
nome, idmateria,

Classe Abtrata Pessoa:
Atributos:
- Nome (Nome da pessoa)
- CPF (CPF da pessoa)
- Email (Email da Pessoa)
- Status (Se está ativo, em espera, demitido ou concluído)

Métodos:
- validacpf()
- validaemail()

Todos esses métodos vão ser codificados na classe mãe, desta forma seus filhos vão herdar esses atributos e métodos já validados e codificados.
O atributo Status significa: Ativo = Aluno ou Professor Ativo, ou seja, faz parte do sistema. Espera = Está aguardando um vaga. Concluído = Aluno formado.  Demitido = Professor Demitido.
O método validacpf() vai considerar apenas o tamanho do CPF, afinal, não é prático realmente fazer um validador de CPF, por motivos de aprendizado.

Classe Aluno(Pessoa):
Atributos:
- Matricula

Métodos:
- calcularmedia()
- calcaprov()
- gerarmatricula()

O método gerarmatricula() cria um atributo Matricula para Aluno, valor é calculado de forma única para cada aluno, sendo um valor sequêncial, toda matricula de aluno deve começar com A. Por exemplo, A1001 -> Primeira matricula de aluno, depois da matricula A1999 deve automaticamente ir para A11000.
O método calcularmedia() calcula a média baseada nas notas do aluno.
O método calcaprov() calcula se o aluno está aprovado ou não com base na média e retorna True ou False, mas não armazena essa informação.

Classe Professor(Pessoa):
Atributos:
- Matricula

Métodos:
- gerarmatricula()

O método gerarmatricula() cria um atributo Matricula para Professor, valor é calculado de forma única para cada professor, sendo um valor sequêncial, toda matricula de professor deve começar com P. Por exemplo, A1001 -> Primeira matricula de aluno, depois da matricula P1999 deve automaticamente ir para P11000.
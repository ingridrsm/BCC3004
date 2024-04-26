# BCC3004

## Visão Geral

- Os princípios escolhidos foram [Princípio de Responsabilidade Única](#princípio-de-responsabilidade-única), [Princípio da Segregação de Interface](#princípio-da-segregação-de-interface), [Princípio Aberto-Fechado](#princípio-aberto-fechado) e [Princípio de Demeter](#princípio-de-demeter).

- A implementação correta de cada um dos princípios está nos arquivos nomeados como *correto.py*, enquanto o exemplo de implementação incorreta está nos arquivos nomeados como *violacao.py*.

### Princípio de Responsabilidade Única

O Princípio de Responsabilidade Única sugere que uma classe tenha apenas uma responsabilidade ou tarefa. Aplicando esse príncipio, temos um código mais coeso e fácil de ser modificado.

No exemplo de violação, temos a classe Atendente que faz regras de negócio, ou seja, calcula o salário do funcionário baseado em horas trabalhadas, e faz também apresentação, ou seja, imprime o relatório de salário e horas trabalhadas do funcionário. Portanto, no exemplo corrigido, temos agora duas outras classes, a classe SalarioMes, que calcula o salário, e a classe RelatorioPagamento, que faz o relatório explicado anteriormente.


### Princípio da Segregação de Interface

O Princípio de Segregação de Interface sugere que um cliente deve implementar apenas as interfaces úteis pra ele, com métodos que eles vão usar. Aplicando esse princípio, temos um código mais coeso e simples, ou seja, mais limpo.

No exemplo de violação, temos a classe Funcionário que possui as responsabilidade de fazer a limpeza do ambiente e cozinhar, e temos a classe Cozinheiro, que teria apenas a responsabilidade de cozinhar, mas não de limpar. Porém, a classe Cozinheiro herda da classe Funcionário, ou seja, o Cozinheiro não vai ativamente usar o método de limpeza, então não havia necessidade de implementar tal método na classe Funcionário. Portanto, no exemplo corrigido, temos agora duas outras classes que herdam de funcionário, a classe Cozinheiro, com a responsabilidade de cozinhar, e a classe Faxineiro, com a responsabilidade de limpar.


### Princípio Aberto-Fechado

O Princípio Aberto-Fechado sugere que uma classe deve ser aberta para extensões e fechada para modificações. Aplicando esse princípio, temos um código de classes mais flexíveis e adaptáveis. 

No exemplo de violação, temos a classe Aula que possui a responsabilidade de "escolher" qual disciplina vai ser ministrada (matemática, biologia ou história). Tal classe não é flexível, uma vez que se, por exemplo, for necessário adicionar a disciplina geografia, sera preciso modificar a classe e adicionar um novo if. Portanto, no exemplo corrigido, temos agora as classes Matematica, Biologia e Historia, onde todas possuem a responsabilidade de ministrar uma aula. Agora é possível criar a classe Geografia sem modificar o código da classe Aula.

### Princípio de Demeter

O Princípio de Demeter sugere que um método B de uma classe A deve apenas invocar os métodos da própria classe A, os objetos passados como parâmetro do método B, os objetos criados pelo método B, os atributos da classe do método B e um método estático. Aplicando esse princípio, temos um código mais fácil de ser entendido.

Tanto no exemplo de violação quanto no exemplo correto temos as classes Oculos, Modelo e Grau. A diferença, é que na violação, pode-se acessar o valor do grau do modelo através diretamente da classe Oculos, sendo que a classe Oculos não deveria conhecer diretamente a classe Grau. Para corrigir, foi adicionado um método em cada uma das classes, chamado obter_grau(), que retorna o valor do grau. Assim, pode-se acessar o valor por meio de tal método e, agora, a classe Oculos não conhece diretamente a classe Grau.

### Autora

  - **Ingrid Reupke**
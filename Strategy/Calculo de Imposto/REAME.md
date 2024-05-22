# Exemplo Strategy

Em uma empresa existem três cargos: desenvolvedor, gerente e dba. Cada um deles possui um salário sobre o qual é aplicado um calculo de imposto diferente.

A classe `CalculaImposto` define uma classe abstrata que conteḿ os métodos comuns aos dois algoritmos possíveis: `CalculaImpostoQuinzeOuDez` e `CalculaImpostoVinteOuQuinze`. Dentro da classe funcionário essas classes são instânciadas a depender do cargo que o funcionário recebe.

Diagrama de Classe
![image](https://github.com/DeividSouSan/Design-Patterns/assets/49818020/90bcf48e-23e5-4127-a8ea-9867665a6700)

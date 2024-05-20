# Exemplo Adapter

O serviço `payment_service` é um **serviço externo** ou **legado** e que não pode ser modificado por algum motivo. Sabemos que seus métodos são `process_payment` e `cancel_payment`.

O problema é que, por algum motivo, dentro do nosso programa principal (`main.py`), há uma interface (contrato) que espera que o serviço de pagamento possua os métodos `execute` e `cancel`. 

Portanto, podemos afirmar que o serviço de pagamento é incompátivel com a interface que o nosso `main.py` espera.

Duas coisas nesse problema são cruciais para que o *adapter* seja necessário:
1. O *serviço de pagamento* não pode ter seu código fonte modificado.
2. O `main.py` por alguma **obrigatoriedade** precisa que o *serviço de pagamento* possua exatamente os métodos `execute` e `cancel`.

A solução é criar um adaptador, uma classe intermediária, que permitirá acessarmos os métodos do *serviço de pagamento* por meio de métodos (`execute` e `cancel`) que satisfaçam a necessidade do `main.py`.
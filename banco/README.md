# Simulador de banco

## Diagrama de classes

```
+-----------------------------------------------+
|                 Banco                         |
+-----------------------------------------------+
| - nome: string                                |
| - agencias: Agencia[]                         |
+-----------------------------------------------+
| + encontrar_agencia(numero: str): list        |
| + adicionar_agencia(agencia_numero: str): str |
| + remover_agencia(agencia_numero: str): str   |
| + listar_agencias(): list                     |
+-----------------------------------------------+

+----------------------------------------+
|               Agencia                   |
+----------------------------------------+
| - numero: string                        |
| - contas: Conta[]                       |
+----------------------------------------+
| + listar_contas(): list                 |
| + encontrar_conta(numero: str): list    |
| + adicionar_conta(): void    |
| + remover_conta(numero: str): void      |
+----------------------------------------+

+----------------------------------------+
|                Conta                    |
+----------------------------------------+
| - numero: string                        |
| - saldo: float                          |
+----------------------------------------+
| + depositar(valor: float): str          |
| + sacar(valor: float): str              |
+----------------------------------------+

```

from typing import Callable
import time


class Conta:
    def __init__(self, numero: str, saldo: float = 0.0) -> None:
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor
        return 'Valor depositado!'

    def sacar(self, valor: float):
        if self.saldo < valor:
            return 'Você não possui saldo suficiente para sacar'

        self.saldo -= valor
        return 'Valor Sacado!'


class Agencia:
    def __init__(self, numero: str, contas: list[Conta] = []) -> None:
        self.numero = numero
        self.contas = contas

    def listar_contas(self) -> str:
        pega_todos_numero: Callable[[Conta],
                                    str] = lambda x: x.numero

        return f'=====Contas da AGÊNCIA {self.numero}======\n' + \
            ', '.join(list(map(pega_todos_numero, self.contas)))

    def encontrar_conta(self, numero: str) -> list:
        encontrar_numero: Callable[[Conta],
                                   bool] = lambda x: x.numero == numero
        conta = list(filter(encontrar_numero, self.contas))
        return conta

    def adicionar_conta(self):
        adicionar_contas = input("Deseja adicionar Contas [y | n]: ")

        while adicionar_contas == 'y':
            conta_numero = input("Numero da Conta: ")
            existe_conta = self.encontrar_conta(conta_numero)

            if len(existe_conta) > 0:
                print("A conta já existe")

            else:
                conta_saldo = float(input("Digite o saldo da conta: "))
                conta = Conta(conta_numero, conta_saldo)

                self.contas.append(conta)
                print("Conta Adicionada a Agência")

            adicionar_contas = input("Deseja adicionar Contas [y | n]: ")

    def remover_conta(self, conta_numero: str):
        encontrar_conta = self.encontrar_conta(conta_numero)
        if len(encontrar_conta) == 0:
            return "A conta não existe"

        conta = encontrar_conta[0]
        self.contas.remove(conta)
        return "Conta Removida com Sucesso!"


class Banco:
    def __init__(self, nome: str, agencias: list[Agencia] = []):
        self.nome = nome
        self.agencias = agencias

    def listar_agencias(self) -> str:
        pega_todos_numero: Callable[[Agencia],
                                    str] = lambda x: x.numero

        return '=====AGÊNCIAS======\n' + \
            ', '.join(list(map(pega_todos_numero, self.agencias)))

    def encontrar_agencia(self, numero: str) -> list:
        encontrar_numero: Callable[[Agencia],
                                   bool] = lambda x: x.numero == numero
        agencia: list = list(
            filter(encontrar_numero, self.agencias))
        return agencia

    def adicionar_agencia(self, agencia_numero: str) -> str:
        encontrar_agencia = self.encontrar_agencia(agencia_numero)
        if len(encontrar_agencia) > 0:
            return "A agencia já existe"

        agencia = Agencia(agencia_numero)
        agencia.adicionar_conta()
        self.agencias.append(agencia)

        return "Agência criada com sucesso!"

    def remover_agencia(self, agencia_numero: str) -> str:
        encontrar_agencia = self.encontrar_agencia(agencia_numero)
        if len(encontrar_agencia) == 0:
            return "A agencia não existe"

        agencia = encontrar_agencia[0]
        self.agencias.remove(agencia)

        return "Agência removida com sucesso!"


class App:
    def __init__(self) -> None:
        conta1 = Conta('1', 200.0)
        conta2 = Conta('2', 0.0)
        conta3 = Conta('3', 30.0)
        contas = [conta1, conta2, conta3]

        agencia1 = Agencia('1', contas)
        agencia2 = Agencia('2', contas)
        agencia3 = Agencia('3')
        agencias = [agencia1, agencia2, agencia3]

        self.banco = Banco("Banco do Brasil", agencias)

    def run_conta(self, agencia):
        conta_numero = input('Número da Conta:')
        encontrar_conta = agencia.encontrar_conta(conta_numero)

        if len(encontrar_conta) > 0:
            conta: Conta = encontrar_conta[0]

            while True:
                print(f"""
                Bem-vindo: conta {conta.numero} 
                agencia {agencia.numero}
                    [1] Depositar em conta
                    [2] Sacar em conta
                    [3 | q] Voltar
                """)
                valor = float(
                    input("Insira um valor: "))
                opcao = input("Selecione uma opcão: ")

                if opcao == '1':
                    resposta = conta.depositar(valor)
                    print(resposta)

                elif opcao == '2':
                    resposta = conta.sacar(valor)
                    print(resposta)

                elif opcao in '3q':
                    print("Saindo...")
                    break
        else:
            print("Essa conta não existe!")

    def run_agencia(self, agencia_numero):
        encontrar_agencia = self.banco.encontrar_agencia(agencia_numero)

        if len(encontrar_agencia) > 0:
            agencia: Agencia = encontrar_agencia[0]

            while True:
                print(f"""  
                    Bem-vindo a Agência {agencia.numero}
                        [1] Adicionar Conta
                        [2] Remover Conta
                        [3] Acessar Conta
                        [4] Listar Contas
                        [5 | q] Voltar
                    """)
                opcao = input("Selecione uma opcão: ")

                if opcao == '1':
                    agencia.adicionar_conta()

                elif opcao == '2':
                    conta_numero = input(
                        "Insira um numero da conta para deletar: ")
                    resposta = agencia.remover_conta(conta_numero)
                    print(resposta)

                elif opcao == '3':
                    self.run_conta(agencia)

                elif opcao == '4':
                    print(agencia.listar_contas())
                    time.sleep(2)

                elif opcao in '5q':
                    print("Saindo...")
                    break
                else:
                    print("Essa opção não existe")
        else:
            print("Esta Agência não existe!")

    def run(self):
        while True:
            print(f"""
            Bem-vindo ao {self.banco.nome}
                O que deseja fazer?
                    [1] Adicionar Agência
                    [2] Remover Agência
                    [3] Acessar Agência
                    [4] Listar Agências
                    [5 | q] Sair
            """)
            opcao = input("Selecione uma opcão: ")
            if opcao == '1':
                agencia_numero = input("Número Agência: ")
                resposta = self.banco.adicionar_agencia(agencia_numero)
                print(resposta)

            elif opcao == '2':
                agencia_numero = input("Número Agência: ")
                resposta = self.banco.remover_agencia(agencia_numero)
                print(resposta)

            elif opcao == '3':
                agencia_numero = input("Número Agência: ")
                self.run_agencia(agencia_numero)

            elif opcao == '4':
                print(self.banco.listar_agencias())
                time.sleep(2)

            elif opcao in '3q':
                print("Saindo...")
                break
            else:
                print("Essa opção não existe")


if __name__ == '__main__':
    app = App()
    app.run()

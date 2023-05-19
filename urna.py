import itertools


class Candidato:
    def __init__(self, _id, nome) -> None:
        self._id = _id
        self.nome = nome


class Urna:
    def __init__(self, candidatos: list[Candidato]) -> None:
        self.votos: list[Candidato] = []
        self.candidatos = candidatos

    def inserir_voto(self, voto):
        cand_ids = list(map(lambda x: x._id, self.candidatos))
        if voto not in cand_ids:
            return "[ERROR] Candidato não cadastrado!"

        for candidato in self.candidatos:
            if voto == candidato._id:
                self.votos.append(candidato)
                return "Candidato cadastrado!"

    def lista_candidatos(self):
        for candidato in self.candidatos:
            print(candidato._id, '-', candidato.nome)

    def resultado(self):
        votos_ordenados = sorted(self.votos, key=lambda x: x._id)
        grupos = itertools.groupby(votos_ordenados, key=lambda x: x.nome)
        resultado = [(nome, len(list(votos_grupo)))
                     for nome, votos_grupo in grupos]

        return resultado

    def printa_resultado(self):
        print("---------Resultado---------")
        for i in self.resultado():
            print(i[0], i[1])
        print(self.total_votos())

    def total_votos(self):
        return f'Total de Votos: {len(self.votos)}'


if __name__ == '__main__':
    bolsonaro = Candidato(1, "Bolsonaro")
    lula = Candidato(2, "Lula")
    ciro = Candidato(3, "Ciro")
    candidatos = [bolsonaro, lula, ciro]

    urna = Urna(candidatos)
    while True:
        print("---------$---------")
        urna.lista_candidatos()

        user = input('Seu voto: ')
        print("")
        if user.lower() == 'sair' or user.lower() == 'q':
            urna.printa_resultado()
            break
        elif user.isdigit():
            print(urna.inserir_voto(int(user)))
        else:
            print('Operação inválida!')

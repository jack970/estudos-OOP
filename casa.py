class Lampada:
    def __init__(self, potencia) -> None:
        self.acesa = False
        self.potencia = potencia

    def mostra_estado(self):
        return self.acesa

    def acende(self):
        if self.acesa:
            print("ERROR! Já Está acesa!")
        else:
            self.acesa = True

    def apaga(self):
        if not self.acesa:
            print("[ERROR! Já está apagada!")
        else:
            self.acesa = False


class Porta:
    def __init__(self, dimensaoY: float, dimensaoX: float, dimensaoZ: float):
        self.aberta = False
        self.cor = None
        self.dimensaoY = dimensaoY
        self.dimensaoX = dimensaoX
        self.dimensaoZ = dimensaoZ

    def pinta(self, p_cor: str):
        self.cor = p_cor
        print(f"Porta pintada com a cor: {p_cor}")

    def mostra_estado(self) -> bool:
        return self.aberta

    def abre(self):
        self.aberta = True

    def fecha(self):
        self.aberta = False


class Casa:
    def __init__(self, num_quartos) -> None:
        self.num_quartos = num_quartos
        self.portas = []
        self.lampadas = []

    def assentar_porta(self, *portas: list):
        for porta in portas:
            self.portas.append(porta)

    def abre_porta(self, p_porta: Porta):
        for i, porta in enumerate(self.portas):
            if porta == p_porta:
                self.portas[i].abre()

    def fecha_porta(self, p_porta: Porta):
        for i, porta in enumerate(self.portas):
            if porta == p_porta:
                self.portas[i].fecha()

    def conta_portas_abertas(self):
        total_portas_abertas = 0
        for porta in self.portas:
            if porta.aberta == True:
                total_portas_abertas += 1
        return total_portas_abertas

    def instala_lampadas(self, *lampadas: list):
        for lampada in lampadas:
            self.lampadas.append(lampada)

    def acende_lampada(self, l_lampada: Lampada):
        if l_lampada in self.lampadas:
            for i, lampada in enumerate(self.lampadas):
                if l_lampada == lampada:
                    self.lampadas[i].acende()
        else:
            print("Não existe essa lâmpada na casa!")

    def apaga_lampada(self, l_lampada: Lampada):
        if l_lampada in self.lampadas:
            for i, lampada in enumerate(self.lampadas):
                if l_lampada == lampada:
                    self.lampadas[i].apaga()
        else:
            print("Não existe essa lâmpada na casa!")

    def conta_lampadas_acesas(self):
        total_lampadas_acesas = 0
        for lampada in self.lampadas:
            if lampada.acesa:
                total_lampadas_acesas += 1
        return total_lampadas_acesas

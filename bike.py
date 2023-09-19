class Bike:
    # aros = [12, 16, 20, 24, 26, 29]
    # vel_max = [15, 20, 25, 30, 60, 70] velocidades imaginárias
    V_MAX = 20  # km/h
    V_MIN = 0  # km/h
    veloc_atual = 0
    altura_cela = 0
    calibragem_peneus = None
    pedalando = False
    peso_max = 110  # kg

    def __init__(self, peso, aro):
        self.peso = peso
        self.aro = aro

    def pedalar(self):
        if not self.pedalando:
            print("Está pedalando...")
            self.pedalando = True
        else:
            print("Ja está pedalando.")

    def parar_de_pedalar(self):
        if self.pedalando:
            print("Parou de pedalar")
            self.pedalando = False
        else:
            print("Ja está parado.")

    def regular_cela(self):
        if self.pedalando:
            print("Você não pode regular a cela agora.")
        else:
            print("Digite o valor em cm para regular a altura da cela:")
            try:
                altura_cela = float(input('>>> '))
            except ValueError:
                print("Valor inválido!")
                sub_op = input('[1] Tentar Novamente\n[2] Voltar')
                if sub_op == '1':
                    self.regular_cela()
            else:
                print(f"Você alterou a altura da cela de {0}cm para {1}cm !".format(
                    self.altura_cela, altura_cela))
                self.altura_cela = altura_cela

    def calibrar_peneus(self):
        if self.pedalando:
            print("Você não pode calibrar os peneus enquando está andando!")
        else:
            print("Digite o valor da pressão de calibragem de seu peneu:")
            try:
                presao = float(input(">>> "))
            except ValueError:
                print('Valor inválido, porfavor digite um valor de pressão válido!')
                print('[1] Tentar Novamente\n[2] Voltar')
                sub_op = input(">>>")
                if sub_op == '1':
                    self.calibrar_peneus()
            else:
                self.calibragem_peneus = presao
                print(f"Você calibrou {presao}psi em seus peneus")
        pass

    def __str__(self) -> str:
        return 'É uma bike'


bike = Bike(26, 50)
bike.pedalar()

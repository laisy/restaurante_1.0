class Reserva:
    def __init__(self, nomeReservista, numeroMesa, dataReservada, horaReservada):
        self.nome_reservou = nomeReservista
        self.numero_mesa = numeroMesa
        self.data_reservada = dataReservada
        self.hora_reservada = horaReservada

    def __str__(self):
        return "Nome de quem reservou: " + str(self.nome_reservou) + "| Numero da Mesa: " +str(self.numero_mesa) + " | Data da Reserva: " + str(self.data_reservada) + "| Hora da Reserva: " + str(hora_reservada)

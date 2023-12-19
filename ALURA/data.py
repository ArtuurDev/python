#você deve criar uma nova classe auxiliar. 
#Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada. 


class Data: 


    def __init__(self, dia, mes, ano):
        self.dia = dia
        self. mes = mes 
        self.ano = ano 

    

    def formatando_data(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))






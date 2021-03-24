import random
import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from main import*
from PyQt5.QtGui import QIcon
class loteria(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_loteria()
        self.ui.setupUi(self)
        #
        self.setWindowIcon(QIcon("iconloteria/trevomega.png"))
        #
        self.ui.roda_roda.clicked.connect(self.numero)
        self.ui.limpar.clicked.connect(self.clear)
    def numero(self):
        self.ui.text_app.setText("CARREGANDO")
        import time
        numero =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
        ,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,
        57,58,59,60]
        random.shuffle(numero)
        self.up()
        self.ui.numero1.setText(str(numero[0]))
        self.ui.numero2.setText(str(numero[1]))
        self.ui.numero3.setText(str(numero[2]))
        self.ui.numero4.setText(str(numero[3]))
        self.ui.numero5.setText(str(numero[4]))
        self.ui.numero6.setText(str(numero[5]))
        QMessageBox.about(self, "Title", "NUMEROS GANHADOR")
        self.musica()
        self.ui.text_app.setText("")
        

        #buttonReply=QMessageBox.question(self, 'MEGA SENHA', "SALVAR", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #if buttonReply==QMessageBox.Yes:
         #   print('bom')
        #if buttonReply==QMessageBox.No:
         #   print('Deu ruim')
    def clear(self):
        self.ui.numero1.setText("")
        self.ui.numero2.setText("")
        self.ui.numero3.setText("")
        self.ui.numero4.setText("")
        self.ui.numero5.setText("")
        self.ui.numero6.setText("")
    def up(self,):#barra de carregamento
        import time, sys
        
        for i in range(0, 101):
            sys.stdout.write("\r{}".format(i))
            sys.stdout.flush()
            time.sleep(0.02)
            self.ui.progressBar.setValue(i)
            
    def musica(self):
        import pygame
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('iconloteria/loteria.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()

        
                

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = loteria()
    window.show()
    app.exec_()
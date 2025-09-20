import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class TransporteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Título y tamaño de ventana
        self.setWindowTitle("Cálculo de gasto en transporte - El Salvador")
        self.setGeometry(200, 200, 400, 250)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # Campos de entrada
        self.lbl_bus = QLabel("Viajes en bus por día:")
        self.txt_bus = QLineEdit()
        
        self.lbl_micro = QLabel("Viajes en microbús por día:")
        self.txt_micro = QLineEdit()
        
        self.lbl_dias = QLabel("Días de viaje por semana:")
        self.txt_dias = QLineEdit()
        
        # Botones
        self.btn_calcular = QPushButton("Calcular gasto")
        self.btn_calcular.clicked.connect(self.calcular_gasto)
        
        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.clicked.connect(self.limpiar_campos)
        
        # Resultado
        self.lbl_resultado = QLabel("Resultado: ")
        
        # Agregar widgets al layout
        layout.addWidget(self.lbl_bus)
        layout.addWidget(self.txt_bus)
        layout.addWidget(self.lbl_micro)
        layout.addWidget(self.txt_micro)
        layout.addWidget(self.lbl_dias)
        layout.addWidget(self.txt_dias)
        layout.addWidget(self.btn_calcular)
        layout.addWidget(self.btn_limpiar)
        layout.addWidget(self.lbl_resultado)
        
        # Establecer layout
        self.setLayout(layout)
    
    def calcular_gasto(self):
        try:
            # Obtener valores
            viajes_bus = int(self.txt_bus.text())
            viajes_micro = int(self.txt_micro.text())
            dias_semana = int(self.txt_dias.text())
            
            # Tarifas en El Salvador
            tarifa_bus = 0.20
            tarifa_micro = 0.25
            
            # Cálculos
            gasto_diario = (viajes_bus * tarifa_bus) + (viajes_micro * tarifa_micro)
            gasto_semanal = gasto_diario * dias_semana
            gasto_mensual = gasto_semanal * 4  # 4 semanas aprox
            
            # Mostrar resultados
            self.lbl_resultado.setText(
                f"Gasto diario: ${gasto_diario:.2f}\n"
                f"Gasto semanal: ${gasto_semanal:.2f}\n"
                f"Gasto mensual (aprox): ${gasto_mensual:.2f}"
            )
        except:
            QMessageBox.warning(self, "Error", "Ingrese solo números válidos.")
    
    def limpiar_campos(self):
        self.txt_bus.clear()
        self.txt_micro.clear()
        self.txt_dias.clear()
        self.lbl_resultado.setText("Resultado: ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TransporteApp()
    ventana.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
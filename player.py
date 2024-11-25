import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.upgrade_level = 1
        self.upgrade_cost = 10
        self.auto_clickers = 0
        self.auto_clicker_cost = 50

        self.initUI()

        self.auto_click_timer = QTimer(self)
        self.auto_click_timer.timeout.connect(self.auto_click)
        self.auto_click_timer.start(1000)

    def initUI(self):
        self.setWindowTitle("Кликер игра на PyQt5")
        self.setGeometry(300, 300, 300, 200)
        self.score_label = QLabel(f"Очки: {self.score}", self)
        self.score_label.setStyleSheet("font-size: 18px;")

        self.click_button = QPushButton("Клик!", self)
        self.click_button.clicked.connect(self.click)

        self.upgrade_button = QPushButton(f"Купить улучшение (+1 к очкам за клик): {self.upgrade_cost}", self)
        self.upgrade_button.clicked.connect(self.buy_upgrade)

        self.auto_clicker_button = QPushButton(f"Купить автокликер: {self.auto_clicker_cost}", self)
        self.auto_clicker_button.clicked.connect(self.buy_auto_clicker)

        vbox = QVBoxLayout()
        vbox.addWidget(self.score_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.click_button)
        vbox.addLayout(hbox)

        vbox.addWidget(self.upgrade_button)
        vbox.addWidget(self.auto_clicker_button)

        self.setLayout(vbox)

    def click(self):
        self.score += self.upgrade_level
        self.update_ui()

    def buy_upgrade(self):
        if self.score >= self.upgrade_cost:
            self.score -= self.upgrade_cost
            self.upgrade_level += 1
            self.upgrade_cost *= 2
        self.update_ui()

    def buy_auto_clicker(self):
        if self.score >= self.auto_clicker_cost:
            self.score -= self.auto_clicker_cost
            self.auto_clickers += 1
            self.auto_clicker_cost *= 2
        self.update_ui()

    def auto_click(self):
        self.score += self.auto_clickers
        self.update_ui()

    def update_ui(self):
        self.score_label.setText(f"Очки: {self.score}")
        self.upgrade_button.setText(f"Купить улучшение (+1 к очкам за клик): {self.upgrade_cost}")
        self.auto_clicker_button.setText(f"Купить автокликер: {self.auto_clicker_cost}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = ClickerGame()
    game.show()
    sys.exit(app.exec_())

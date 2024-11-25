import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Кликер игра")

        self.score = 0
        self.upgrade_level = 1
        self.upgrade_cost = 10

        self.auto_clickers = 0
        self.auto_clicker_cost = 50

        # Создаем виджеты интерфейса
        self.score_label = tk.Label(root, text=f"Очки: {self.score}", font=("Helvetica", 24))
        self.score_label.pack(pady=20)

        self.click_button = tk.Button(root, text="Клик!", font=("Helvetica", 24), command=self.click)
        self.click_button.pack(pady=20)

        self.upgrade_button = tk.Button(root, text="Купить улучшение (+1 к очкам за клик)", font=("Helvetica", 14), command=self.buy_upgrade)
        self.upgrade_button.pack(pady=10)

        self.upgrade_label = tk.Label(root, text=f"Цена улучшения: {self.upgrade_cost}", font=("Helvetica", 14))
        self.upgrade_label.pack(pady=10)

        self.auto_clicker_button = tk.Button(root, text="Купить автокликер", font=("Helvetica", 14), command=self.buy_auto_clicker)
        self.auto_clicker_button.pack(pady=10)

        self.auto_clicker_label = tk.Label(root, text=f"Цена автокликера: {self.auto_clicker_cost}", font=("Helvetica", 14))
        self.auto_clicker_label.pack(pady=10)

        self.auto_click()

    def click(self):
        self.score += self.upgrade_level
        self.score_label.config(text=f"Очки: {self.score}")

    def buy_upgrade(self):
        if self.score >= self.upgrade_cost:
            self.score -= self.upgrade_cost
            self.upgrade_level += 1
            self.upgrade_cost *= 2
            self.score_label.config(text=f"Очки: {self.score}")
            self.upgrade_label.config(text=f"Цена улучшения: {self.upgrade_cost}")
        else:
            self.upgrade_label.config(text=f"Недостаточно очков. Нужно: {self.upgrade_cost}")

    def buy_auto_clicker(self):
        if self.score >= self.auto_clicker_cost:
            self.score -= self.auto_clicker_cost
            self.auto_clickers += 1
            self.auto_clicker_cost *= 2
            self.score_label.config(text=f"Очки: {self.score}")
            self.auto_clicker_label.config(text=f"Цена автокликера: {self.auto_clicker_cost}")
        else:
            self.auto_clicker_label.config(text=f"Недостаточно очков. Нужно: {self.auto_clicker_cost}")

    def auto_click(self):
        self.score += self.auto_clickers
        self.score_label.config(text=f"Очки: {self.score}")
        self.root.after(1000, self.auto_click)  # Автоклик каждые 1 секунду

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()

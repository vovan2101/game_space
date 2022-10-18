class Stats():
    # Отслеживание статистики
    def __init__(self):
        # Инициализирует статистику
        self.reset_stats()
    
    def reset_stats(self):
        # Статистика изменяющиеся во время игры
        self.guns_left = 2

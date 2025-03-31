import random

# Размер поля
SIZE = 10

# Символы для отображения
EMPTY = 'O'
SHIP = '■'
HIT = 'X'
MISS = 'T'

# Класс для создания игрового поля
class Board:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
        self.ships = []
    
    # Размещение корабля на поле
    def place_ship(self, ship_size):
        while True:
            x = random.randint(0, SIZE - 1)
            y = random.randint(0, SIZE - 1)
            direction = random.choice(['horizontal', 'vertical'])
            
            if self.can_place_ship(x, y, ship_size, direction):
                self.add_ship(x, y, ship_size, direction)
                break
    
    # Проверка возможности размещения корабля
    def can_place_ship(self, x, y, size, direction):
        if direction == 'horizontal':
            if x + size > SIZE:
                return False
            for i in range(x, x + size):
                if self.grid[y][i] != EMPTY:
                    return False
        else:
            if y + size > SIZE:
                return False
            for j in range(y, y + size):
                if self.grid[j][x] != EMPTY:
                    return False
        return True
    
    # Добавление корабля на поле
    def add_ship(self, x, y, size, direction):
        ship_cells = []
        if direction == 'horizontal':
            for i in range(x, x + size):
                self.grid[y][i] = SHIP
                ship_cells.append((i, y))
        else:
            for j in range(y, y + size):
                self.grid[j][x] = SHIP
                ship_cells.append((x, j))
        self.ships.append(ship_cells)
    
    # Вывод поля (скрывает корабли компьютера)
    def display(self, hide_ships=True):
        print("   " + " ".join([chr(65 + i) for i in range(SIZE)]))  # A, B, C, ...
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                cell = self.grid[i][j]
                if hide_ships and cell == SHIP:
                    row.append(EMPTY)
                else:
                    row.append(cell)
            print(f"{i + 1:2} " + " ".join(row))

    
        # Проверка попадания
    def check_hit(self, x, y):
        if self.grid[y][x] == SHIP:
            self.grid[y][x] = HIT
            for ship in self.ships:
                if (x, y) in ship:
                    ship.remove((x, y))
                    if not ship:
                        print("Корабль потоплен!")
                    else:
                        print("Попадание!")
                    return True
        elif self.grid[y][x] == EMPTY:
            self.grid[y][x] = MISS
            print("Мимо!")
            return False
        else:
            print("Уже стреляли сюда!")
            return False

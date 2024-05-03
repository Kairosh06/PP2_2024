import pygame
import random
import psycopg2
import pygame_menu

pygame.init()

conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="2006",
    port = 5432
)
cur = conn.cursor()
conn.commit()

class Snake:
    def _init_(self):
        self.body = [(7, 10), (6, 10), (5, 10)]
        self.direction = (1, 0)
        self.eaten = False

    def move(self):
        if self.eaten:
            new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
            self.body.insert(0, new_head)
            self.eaten = False
        else:
            new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
            self.body.pop()
            self.body.insert(0, new_head)

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

class Fruit:
    def _init_(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))

    def respawn(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))

class Game:
    def _init_(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0
        self.level = 1
        self.speed = 10
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((400, 400))

    def update(self):
        self.snake.move()
        self.check_collision()
        self.update_level()

    def update_level(self):
        if self.score % 50 == 0 and self.score != 0:
            self.level += 1
            self.speed += 2  # Увеличьте скорость змеи на каждом уровне
            print(f"Level up! You are now on level {self.level}")

    def check_collision(self):
        if self.snake.body[0] == self.fruit.position:
            self.snake.eaten = True
            self.score += 1
            self.fruit.respawn()

    def game_over(self):
        head = self.snake.body[0]
        if (
            head[0] < 0 or head[0] >= 20 or
            head[1] < 0 or head[1] >= 20 or
            head in self.snake.body[1:]
        ):
            return True
        return False

def start_game():
    # Функция запуска игры
    game = Game()
    direction_map = {
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1),
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0)
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key in direction_map:
                    game.snake.change_direction(direction_map[event.key])

        game.update()

        if game.game_over():
            cur.execute(f"INSERT INTO snakescore (username, userscore) VALUES ('{user_name}', {game.score})")
            conn.commit()
            pygame.quit()
            return

        game.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render(f"Level: {game.level}", True, (255, 255, 255))
        game.screen.blit(text, (10, 10))
        text = font.render(f"Score: {game.score}", True, (255, 255, 255))
        game.screen.blit(text, (10, 50))

        for segment in game.snake.body:
            pygame.draw.rect(game.screen, (0, 255, 0), (segment[0] * 20, segment[1] * 20, 20, 20))
        pygame.draw.rect(game.screen, (255, 0, 0), (game.fruit.position[0] * 20, game.fruit.position[1] * 20, 20, 20))
        pygame.display.flip()
        game.clock.tick(game.speed)

def name_checker(NAMEBOX):
    # Функция проверки имени пользователя и запуска игры
    global user_name
    user_name = str(NAMEBOX.get_value())
    cnt = 0
    cur.execute("SELECT * FROM snakescore")
    data = cur.fetchall()

    for row in data:
        if user_name == str(row[1]):
            cnt += 1
    if cnt > 0:
        print(f"User with this name already exists. Level of this user: {int(row[2]) // 3}. Please enter another name.")
    else:
        start_game()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))

menu = pygame_menu.Menu('Welcome', 400, 400, theme=pygame_menu.themes.THEME_BLUE)
name_box = menu.add.text_input('Name:', default='username')
menu.add.button('Play', name_checker, name_box)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
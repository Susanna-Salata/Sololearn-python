class Enemy:
    name = ""
    lives = 0

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + ' killed')
        else:
            print(self.name + ' has ' + str(self.lives) + ' lives')


class Monster(Enemy):

    def __init__(self):
        super().__init__('Monster', 3)


class Alien(Enemy):

    def __init__(self):
        super().__init__('Alien', 5)

def main():

    m = Monster()
    a = Alien()

    while True:
        x = input('Please select from "laser", "gun", "exit" ')
        if x == 'exit':
            break
        elif x == 'laser':
            a.hit()
        elif x == 'gun':
            m.hit()
        else:
            print('Incorrect input. Please select from "laser", "gun", "exit"')


if __name__ == "__main__":
    main()

class Pizza:
    name: str
    dough: str
    sauce: str
    toppings = []

    def prepare(self):
        print('Готовим', self.name)
        print('Месим тесто...')
        print('Добавляем соус...')
        print('Добавляем начинки:')
        for t in self.toppings:
            print('\t', t)

    def bake(self):
        print('Запекаем 25 минут при 350 градусах')

    def cut(self):
        print('Нарезаем пиццу треугольниками')

    def box(self):
        print('Помещаем пиццу в фирменную упаковку')

    def getName():
        return self.name

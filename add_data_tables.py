# Используем Django shell для записи данных
# Откройте Django shell

# python manage.py shell

from task1.models import Buyer, Game
from datetime import date

# Создание записей Buyer
buyer1 = Buyer.objects.create(name="Alice", age=25, balance=100.00)
buyer2 = Buyer.objects.create(name="Bob", age=30, balance=200.00)
buyer3 = Buyer.objects.create(name="Charlie", age=16, balance=50.00)

# Создание записей Game
game1 = Game.objects.create(title="Game A", cost=29.99, size=1.50, description="Description A", age_limited=True)
game2 = Game.objects.create(title="Game B", cost=49.99, size=2.00, description="Description B", age_limited=True)
game3 = Game.objects.create(title="Game C", cost=19.99, size=1.00, description="Description C", age_limited=False)

# Связывание покупателей с играми
# Покупатель 1 (Alice) будет обладать всеми играми
game1.buyer.add(buyer1)
game2.buyer.add(buyer1)
game3.buyer.add(buyer1)

# Покупатель 2 (Bob) будет обладать только ограниченными играми
game1.buyer.add(buyer2)
game2.buyer.add(buyer2)

# Покупатель 3 (Charlie) будет обладать только игрой без ограничения возраста
game3.buyer.add(buyer3)

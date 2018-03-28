# Тренды Github

Скрипт выводит список ТОП-20 репозиториев недели на [github.com](https://github.com). Критерий: количество звезд.
 Рейтинг включает количество открытых задач для каждого репозитория.

### Пример

```bash
> python github_trending.py
  1: UnityCsReference               stars=2505   открыто issues=0    https://github.com/Unity-Technologies/UnityCsReference
  2: GameNetworkingSockets          stars=1093   открыто issues=0    https://github.com/ValveSoftware/GameNetworkingSockets
 ....
 19: figma-api-demo                 stars=102    открыто issues=2    https://github.com/figma/figma-api-demo
 20: person-blocker                 stars=91     открыто issues=2    https://github.com/minimaxir/person-blocker
```
# Требования
Совестимые OC:
* Linux,
* Windows
* MacOS

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 выше

И  пакетов из requirements.txt
```bash
pip install -r requirements.txt # или командой pip3
```

# Как работать
> Запуск для всех ОС одинаковый
Стандатной командой `python` (на некоторых компьютерах `python3`).
```bash
$ python github_trending.py
```

Помните, рекомендуется использовать [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) для лучшего управления пакетами.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

 ___Решение тестового задания "Менеджер учета расходов"___ 
 
 __Для решения задачи было реализовано API с помощью DRF.__
 
 __Файл с решение второго задания называется SQL-TASK__

__Как установить проект__

***
Клонировать репозиторий и перейти в него в командной строке:

~~~
git clone https://github.com/Povladislav/counterApp.git
cd counterApp
~~~

Создать и активировать виртуальное окружение:

~~~
python -m venv venv
source venv/bin/activate
~~~

Установить зависимости из файла requirements.txt:

~~~
pip install -r requirements.txt
~~~

Выполнить миграции:

~~~
cd counter
docker-compose run web python3 manage.py makemigrations
docker-compose run web migrate
~~~

Cбилдить контейнер и запустить проект:
~~~
docker-compose build
docker-compose up
~~~

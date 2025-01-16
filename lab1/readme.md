Инстукция по запуску

1. Перейдите в папку **python** через терминал, создайте и активуруйте виртуальное окружение:
```shell
cd ./python
python -m venv ppenv
.\ppenv\Scripts\activate
```
2. Установите зависимости python
```shell
pip install -r requirements.txt
```
3. Перейдите в папку **c++** через терминал и соберите код через g++, запустите код:
```shell
cd ../c++
g++ exp.cpp -o exp -fopenmp
./exp
```
4. Вернитесь в папку **python**, запустите скрипт:
```shell
cd ../python
python graph.py
```
# Диспетчер хранилищ
Инструкция по запуску программы

## Общая информация

Программа поддерживает работу с Redis и файлами .txt. Неограничивая себя, можно реализовать поддержку с другими хранилищами: SQL БД
(SQLite, PostgreSQL и тд) и другими NoSQL БД (Redis был взят за пример).

### Функционал и особенности

1)

 data состоит из key_name - необходим для ключа в RedisHandler и участвует при записи в файл FileHandler (создание имени файла):

```
	data = {key_name: obj}
```

2) 
Имеются 2 протокола для сериализации.десериализации даннх.
В зависимости от того, какой ключь будет передан в функцию для записи/чтения, будет выполнена соответствующая сериализация/десериализация (Каким протоколом сеарелизуешь данные, таким и десереализушь их, разными Не получится это сделать):
```
	protocols = {"json": JsonSerializer, "pickle": PickleSerializer}
```

3)
Функция для сохранения объекта. Принимает: ссылку на данные,
тип сериализации объекта, имя хранилища:
```
	def worker_saver(data, name_serialize, storage_name)
```
4)
Функция для  получения объекта из хранилища. Принимает: ссылку на данные, тип сериализации объекта, имя хранилища:
```
	def worker_reciver(data, name_serialize, storage_name):
```
5)
Используя Redis, как хранилище, необходимо установить redis-server на локальную машину или использовать Docker. В моем случае redis-server был установлен на локальном ПК. Поддержка для Mack OS, Linux 

```
					https://redis.io/download
```
Обязательно убедитесь, что redis-server запущен, иначе взаимодействовать с данным хранилищем не получится
```
			 	@user:~/MyDataBases/redis/redis-5.0.7$ src/redis-server
```

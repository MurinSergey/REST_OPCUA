Структуру настроек взял из статьи:
https://habr.com/ru/articles/866536/

Для того, чтобы получить непосредственно значение, хранимое типом SecretStr, нужно воспользоваться методом get_secret_value(), например:
Config.load().db.password.get_secret_value()
#db-password-123
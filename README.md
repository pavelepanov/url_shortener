# Url shortener

## Как запустить?

1. Склонировать проект \
```git clone https://github.com/pavelepanov/url_shortener```
2. Создать виртуальное окружение \
```python3 -m venv venv```
3. Установить зависимости \
```pip install -r requirements.txt```
4. Запустить проект, как распространяемый пакет \
```python3 -m url_shortener.entrypoint.http_server ```

## Как тестировать?
Можно выбрать, к примеру, postman или напрямую через терминал с помощью curl
### Пример с curl
1. Создать короткую ссылку на основе полной ссылки и получить короткую ссылку\
```curl -X POST -d '{"key": "http://localhost:8080"}' -H "Content-Type: application/json" http://localhost:8080```
2. Получить полную ссылку по короткой ссылке. Короткую ссылку можно получить после её создания \
```curl "http://localhost:8080/greet?full_url=my_site/37d007"```

![post](/docs/POST.jpg "POST example")
![get](/docs/GET.jpg "GET example")

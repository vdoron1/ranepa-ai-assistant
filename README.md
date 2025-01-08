# Прототип AI-ассистента президентской академии 

__Установка:__

```shell
 chmod +x ./llm/entrypoint.sh
 poetry install
```

__Запуск (prod):__
```shell
docker-compose up
```

__Запуск (dev):__
```shell
docker-compose -f docker-compose.dev.yml up
make run 
```
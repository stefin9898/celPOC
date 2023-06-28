# celPOC

Run RabbitMQ
```
docker run -d -p 5672:5672 rabbitmq
```

Run HTTP Mock Server
```
go run server.go
```
Run Celery Worker
```
celery -A tasks worker --loglevel=INFO
```
Send Celery task to RabbitMQ
```
python main.py
```
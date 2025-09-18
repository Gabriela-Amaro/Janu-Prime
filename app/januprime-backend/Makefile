APP=docker compose exec app

migration:
	$(APP) python manage.py makemigrations

migrate:
	$(APP) python manage.py migrate

superuser:
	$(APP) python manage.py createsuperuser

exec:
	$(APP) 

root: 
	docker compose exec -u 0 app

shell:
	$(APP) shell

fmt:
	$(APP) black . 
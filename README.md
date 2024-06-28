# flask-base
Boilerplate Flask Application with Docker, Nginx, and Gunicorn Configs

## Git Commands

```
git clone https://github.com/PhilipJPrice/flask-base.git
git status
git add file_name.ext
git commit -m "message"
git push
```

## Create Virtual Environment for Libraries (Mac)

```
python3 -m venv venv

source venv/bin/activate

pip install requirements.txt
```

## Add Environment Variables

```
vim env.sample
```

copy code

```
vim .env
```

paste code

save file

## Run Docker

```
docker-compose up --build
```

localhost:7000

## (Or if Docker not Installed) Run Flask Application

flask run

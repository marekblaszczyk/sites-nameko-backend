### Microservice installation:

Clone this repo and create virtualenv.

Install requirements.txt

```
$ pip install -r requirements.txt
```

Create and modified config file

```
$ cp </path/to/app/dir>/config/local-example.yaml </path/to/app/dir>/config/local.yaml
```

If you need change amqp path you can do it in local.yaml

Run microservice
```
$ nameko run --config config/local.yaml app.app
OR
$ fab run_app
```


### MongoDB installation:

The easiest way to get mongodb is official docker container:

```
$ mkdir </path/to/app/dir>/db_data
$ docker run -d --name sites_mongo -p 27017:27017 -v </path/to/app/dir>/db_data:/data/db mongo
```


### RabbitMQ installation:

```
$ docker run -d --hostname my-rabbit --name sites-amqp -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```


### Add example data to MongoDB:

```
$ cd </path/to/app/dir>/scripts
$ python insert_data.py
```

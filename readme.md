### MongoDB

The easiest way to get mongodb is official docker container:

```
mkdir </path/to/app/dir>/db_data
docker run -d --name sites_mongo -p 27017:27017 -v </path/to/app/dir>/db_data:/data/db mongo
```
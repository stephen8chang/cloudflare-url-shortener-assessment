This is my submission for the Cloudflare URL Shortener assessment. Written in Python, it uses FastAPI, Redis, PostgreSQL. Containerized with Docker.

Make sure Docker Desktop is installed.

Clone the repo.

```
git clone https://github.com/your-repo/cloudflare-url-shortener.git
cd cloudflare-url-shortener
```

Build and start containers.
```
docker-compose up --build
```


To stop the containers:
```
docker-compose down
```

### Endpoints

#### Shorten URL
`Invoke-RestMethod -Uri "http://localhost:8000/shorten" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"long_url": "https://example.com"}'`
##### Example response: 
`{"short_url": "http://localhost:8000/abcd1234"}`

#### Retrieve Original URL
`Invoke-RestMethod -Uri "http://localhost:8000/abcd1234" -Method Get`

#### Delete 
`Invoke-RestMethod -Uri "http://localhost:8000/abcd1234" -Method Delete`


### Run Unit Tests Inside The Docker Container
```
docker exec -it cloudflare-url-shortener-app-1 pip install pytest
docker exec -it cloudflare-url-shortener-app-1 pip install httpx
docker exec -it cloudflare-url-shortener-app-1 pytest tests/
```




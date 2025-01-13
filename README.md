#### build & run

```
docker build -t my-django-app .
docker run -d -p 8000:8000 --name my-django-container my-django-app
```

#### features

* Customized Admin Pannel
* JWT Authentication
* Permission
* Filter
* Search
* Sort
* Pagination
* Hyper Link Serializer
* Swagger Documentation
* Dynamic Fields (http://127.0.0.1:8000/api/v1/article/?fields=title,status)

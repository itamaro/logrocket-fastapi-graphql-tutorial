# logrocket-fastapi-graphql-tutorial

Educational project - learning to build a GraphQL server using FastAPI, Graphene, uvicorn

Based on https://blog.logrocket.com/building-a-graphql-server-with-fastapi/

Dockerizing FastAPI for Google Cloud Run based on https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

Google Cloud Run build & deploy based on https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python

## Local Dev with virtualenv

Requires Python 3.6+ (tested with Python 3.9 on MacOS)

```
git clone git@github.com:itamaro/logrocket-fastapi-graphql-tutorial.git
cd logrocket-fastapi-graphql-tutorial
python3 -m venv fastapi-graphql-venv
source fastapi-graphql-venv/bin/activate
pip install fastapi uvicorn graphene
cd fastapi-graphql
uvicorn main:app --reload
```

GraphiQL should be accessible on http://localhost:8000/

## Build & Run Locally With Docker

```
docker build -t fastapi-graphql-app -f docker/Dockerfile .
docker run -it --rm -v $PWD/fastapi-graphql:/app -p 8000:80 fastapi-graphql-app /start-reload.sh
```

GraphiQL should be accessible on http://localhost:8000/

## Build & Deploy On Google Cloud Run

```
export PROJECT_ID="$( gcloud config get-value project )"
gcloud builds submit
gcloud run deploy fastapi-graphql-demo --image=gcr.io/$PROJECT_ID/fastapi-graphql-app --platform=managed --allow-unauthenticated
```

GraphiQL should be accessible on https://fastapi-graphql-demo-mrbe4zqmdq-uw.a.run.app/

## Testing in GraphiQL

Example getCourses query:

```
query GetCoursesQuery {
  getCourses(id: "3") {
    id
    title
    instructor
    publishDate
  }
}
```

Example createCourse mutation:

```
mutation CreateCourseMutation {
  createCourse(
    id: "11"
    title: "Python Lists"
    instructor: "Jane Melody"
  ) {
    course {
      id
      title
      instructor
    }
  }
}
```

## Testing with curl

```
>curl 'https://fastapi-graphql-demo-mrbe4zqmdq-uw.a.run.app/' -XPOST -H "Content-Type: application/json" --data '{"query":"query GetCoursesQuery { getCourses { id title instructor publishDate } }","variables":null,"operationName":"GetCoursesQuery"}'
{"data":{"getCourses":[{"id":"1","title":"Python variables explained","instructor":"Tracy Williams","publishDate":"12th May 2020"},{"id":"2","title":"How to use functions in Python","instructor":"Jane Black","publishDate":"9th April 2018"},{"id":"3","title":"Asynchronous Python","instructor":"Matthew Rivers","publishDate":"10th July 2020"},{"id":"4","title":"Build a REST API","instructor":"Babatunde Mayowa","publishDate":"3rd March 2016"},{"id":"11","title":"Python Lists","instructor":"Jane Melody","publishDate":null}]}}
```

Using `jq` for pretty printing:

```
>curl 'https://fastapi-graphql-demo-mrbe4zqmdq-uw.a.run.app/' -XPOST -H "Content-Type: application/json" --data '{"query":"query GetCoursesQuery { getCourses { id title instructor publishDate } }","variables":null,"operationName":"GetCoursesQuery"}' | jq -C
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   661  100   526  100   135   5057   1298 --:--:-- --:--:-- --:--:--  6355
{
  "data": {
    "getCourses": [
      {
        "id": "1",
        "title": "Python variables explained",
        "instructor": "Tracy Williams",
        "publishDate": "12th May 2020"
      },
      {
        "id": "2",
        "title": "How to use functions in Python",
        "instructor": "Jane Black",
        "publishDate": "9th April 2018"
      },
      {
        "id": "3",
        "title": "Asynchronous Python",
        "instructor": "Matthew Rivers",
        "publishDate": "10th July 2020"
      },
      {
        "id": "4",
        "title": "Build a REST API",
        "instructor": "Babatunde Mayowa",
        "publishDate": "3rd March 2016"
      },
      {
        "id": "11",
        "title": "Python Lists",
        "instructor": "Jane Melody",
        "publishDate": null
      }
    ]
  }
}
```

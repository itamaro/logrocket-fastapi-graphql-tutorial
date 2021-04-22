# logrocket-fastapi-graphql-tutorial

Educational project - learning to build a GraphQL server using FastAPI, Graphene, uvicorn

Based on https://blog.logrocket.com/building-a-graphql-server-with-fastapi/

```
git clone git@github.com:itamaro/logrocket-fastapi-graphql-tutorial.git
cd logrocket-fastapi-graphql-tutorial
python3 -m venv fastapi-graphql-venv
source fastapi-graphql-venv/bin/activate
pip install fastapi uvicorn graphene
uvicorn main:app --reload
```

GraphiQL should be accessible on http://127.0.0.1:8000/

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

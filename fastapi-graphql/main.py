import json

from fastapi import FastAPI
from graphene import Field, List, ObjectType, Schema, String
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
import uvicorn

from schemas import CourseType


class Query(ObjectType):
    course_list = None
    get_courses = Field(List(CourseType), id=String())

    async def resolve_get_courses(self, info, id=None):
        with open("./courses.json") as courses:
            course_list = json.load(courses)
        if id is None:
            return course_list
        return [course for course in course_list if course["id"] == id]


app = FastAPI()
app.add_route(
    "/", GraphQLApp(schema=Schema(query=Query), executor_class=AsyncioExecutor)
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

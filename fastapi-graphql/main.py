import json

from fastapi import FastAPI
from graphene import Field, List, Mutation, ObjectType, Schema, String
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


class CreateCourse(Mutation):
    course = Field(CourseType)

    class Arguments:
        id = String(required=True)
        title = String(required=True)
        instructor = String(required=True)

    async def mutate(self, info, id, title, instructor):
        with open("./courses.json", "r+") as courses:
            course_list = json.load(courses)
            course_list.append({"id": id, "title": title, "instructor": instructor})
            courses.seek(0)
            json.dump(course_list, courses, indent=2)
        return CreateCourse(course=course_list[-1])


class Mutation(ObjectType):
    create_course = CreateCourse.Field()


app = FastAPI()
app.add_route(
    "/",
    GraphQLApp(
        schema=Schema(query=Query, mutation=Mutation), executor_class=AsyncioExecutor
    ),
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

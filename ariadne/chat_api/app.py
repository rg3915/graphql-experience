# https://www.twilio.com/blog/graphql-api-subscriptions-python-asyncio-ariadne
from ariadne.asgi import GraphQL
from mutations import mutation
from queries import query
from subscriptions import subscription

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers
)

type_defs = load_schema_from_path("schema.graphql")

schema = make_executable_schema(type_defs, query, mutation, subscription, snake_case_fallback_resolvers)  # noqa E501
app = GraphQL(schema, debug=True)


# @query.field("hello")
# def resolve_hello(*_):
#     return "Hello world!"

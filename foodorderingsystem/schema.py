import graphene

from graphene_django.debug import DjangoDebug

import fos.schema


class Query(fos.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(fos.schema.Mutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)
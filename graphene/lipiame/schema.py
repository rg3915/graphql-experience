import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.orm import scoped_session, sessionmaker
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.routing import Route

from models import Campaign, engine

Session = scoped_session(sessionmaker(bind=engine))


class CreateCampaign(graphene.Mutation):
    id = graphene.Int()
    campaign_name = graphene.String()
    user_email = graphene.String()

    class Arguments:
        campaign_name = graphene.String()
        user_email = graphene.String()

    def mutate(self, info, user_email, campaign_name):
        session = Session()
        campaign = Campaign(user_email=user_email, campaign_name=campaign_name)
        session.add(campaign)
        session.commit()

        return CreateCampaign(
            id=campaign.id,
            campaign_name=campaign.campaign_name,
            user_email=campaign.user_email,
        )


class Mutation(graphene.ObjectType):
    create_campaign = CreateCampaign.Field()


class CampaignType(SQLAlchemyObjectType):
    class Meta:
        model = Campaign


class Query(graphene.ObjectType):
    campaign = graphene.List(CampaignType, user_email=graphene.String())

    def resolve_campaign(self, info, user_email):
        session = Session()
        campaign = session.query(Campaign).filter(
            Campaign.user_email == user_email).all()
        return campaign


routes = [
    Route('/', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))
]

app = Starlette(routes=routes)

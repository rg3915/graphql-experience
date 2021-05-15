## GraphQL With Python

https://test.decoded.africa/graphql-the-python-experience/

```
pip install fastapi sqlalchemy graphene graphene-sqlalchemy uvicorn
```

```
uvicorn schema:app --host 127.0.0.1 --port 8000
```



```
mutation {
  createCampaign(campaignName: "Um", userEmail: "regis@email.com") {
    campaignName
    userEmail
  }
}
```


```
{
  campaign(userEmail: "regis@email.com") {
    id
    amountContributed
    campaignName
    userEmail
  }
}

```


## Tutorial 1: Build a GraphQL API with Subscriptions using Python, Asyncio and Ariadne

https://www.twilio.com/blog/graphql-api-subscriptions-python-asyncio-ariadne


```
pip install ariadne "uvicorn[standard]"
```


```
uvicorn app:app --reload
```


```
mutation {
  createUser(username:"user_one") {
    success
    user {
      userId
      username
    }
  }
}

subscription {
  messages(userId: "2") {
    content
    senderId
    recipientId
  }
}

mutation {
  createMessage(
    senderId: "1",
    recipientId: "2",
    content:"Hello there"
  ) {
    success
    message {
      content
      recipientId
      senderId
    }
  }
}
```


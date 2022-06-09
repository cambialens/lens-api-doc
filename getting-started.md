---
layout: post-sidebar
title: Getting Started
permalink: /getting-started.html
show_sidebar: true
sidebar: toc
toc:
  - title: Table of Contents
    subfolderitems:
      - page: Prerequisites
        url: getting-started.html#prerequisites
      - page: API Resources
        url: getting-started.html#api-resources
      - page: API Access
        url: getting-started.html#api-access
      - page: Rate Limiting
        url: getting-started.html#rate-limiting
      - page: HTTP Responses
        url: getting-started.html#http-responses
---

### Prerequisites

You need to have the following before you can start using Lens APIs:

1. Granted access to our API service ([request access](https://www.lens.org/lens/user/subscriptions)).
2. Create an Access Token from your user profile page.
3. Basic knowledge of API structure and JSON formatting.
4. Any API Client (cURL, Postman, etc.)

### API Resources

As of the current version, Lens offers the following API endpoints:

**Patents:** 
- `[POST] https://api.lens.org/patent/search`
- `[GET] https://api.lens.org/patent/search`
- `[GET] https://api.lens.org/patent/{lens_id}`

**Patent Data Schema:** 
- `[POST] https://api.lens.org/schema/patent`
- `[GET] https://api.lens.org/schema/patent`

**Scholarly Works:** 
- `[POST] https://api.lens.org/scholarly/search`
- `[GET] https://api.lens.org/scholarly/search`
- `[GET] https://api.lens.org/scholarly/{lens_id}`

**Scholarly Works Data Schema:** 
- `[POST] https://api.lens.org/schema/scholarly`
- `[GET] https://api.lens.org/schema/scholarly`

**Collections:** 
- `[POST] https://api.lens.org/collections/{collection_id}`
- `[GET] https://api.lens.org/collections/{collection_id}`

> You can access scholarly works in your collections from your [Work Area]. The `{collection_id}` can be found at the end of your collection URL, e.g. `https://www.lens.org/lens/scholar/search/results?collectionId={collection_id}`.
> Here is an [example](examples-scholar.html#access-your-collection) to illustrate how to access your collection.

**API usage:** 
- `[GET] https://api.lens.org/subscriptions/patent_api/usage`
- `[GET] https://api.lens.org/subscriptions/scholarly_api/usage`


**Swagger Documentation is available here:** [https://api.lens.org/swagger-ui.html](https://api.lens.org/swagger-ui.html)


### API Access

Your use of the API is subject to the Lens [Terms of Use]. Lens uses token-based API authentication, you can request access and [manage your access plan and tokens] from your Lens user profile.

For `POST` Requests, you need to provide your access token in the Request Header when accessing the APIs:
>Example: ```Authorization: Bearer your-access-token```

For `GET` Requests, you can provide your access token in the request parameter:
>Example: ```https://api.lens.org/scholarly/search?token=your-access-token```

### Rate Limiting

To ensure our public API endpoints remain usable by everyone and to maintain the server's optimal availability, a rate limiting mechanism is being used to temporarily block any clients that reduce the server's performance. The applied rate limits will be included in the following HTTP response headers:

- `x-rate-limit-remaining-request-per-minute`: Number of remaining requests allowed in a minute
- `x-rate-limit-retry-after-seconds`: Time in seconds until next request can be performed
- `x-rate-limit-reset-date`: Rate limit will get reset at this date
- `x-rate-limit-remaining-request-per-month`: Number of API calls allowed till the reset date above
- `x-rate-limit-remaining-record-per-month`: Number of remaining records that can be fetched

Once you go over any rate limit you will receive a `429 - Too many requests` error with respective messages.

### HTTP Responses

Response |  Description  |  
 ------- | -------|
200 - Ok | Valid response from the server
400 - Bad Request | Malformed request or incorrect fields/values provided
401 - Unauthorized | Authentication credentials might be incorrect or missing
404 - Not Found | Incorrect Resource URL / Empty Result for supplied queries / Expired `scroll_id`
415 - Unsupported Media Type | Request body is not json or `Content Type` is not `application/json`
429 - Too Many Requests | You have exceeded the number of allowed calls
50x	- Internal Server Error	| An error occurred on API server side.

[manage your access plan and tokens]: <http://lens.org/lens/user/subscriptions>
[Terms of Use]: <https://about.lens.org/policies/#termsuse>
[Work Area]: <https://www.lens.org/lens/user/collections>

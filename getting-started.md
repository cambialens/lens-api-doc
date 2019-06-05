---
layout: page
title: Getting Started
permalink: /getting-started/
---

{:.table-contents}
- [Prerequisites](#prerequisites)
- [API Endpoints](#api-endpoints)
- [API Access](#api-access)
- [Rate Limiting](#rate-limiting)
- [HTTP Responses](#http-responses)


### Prerequisites

You need to have the following before you can start using Lens APIs:

1. Subscribed to our API service.
2. Create Access Token from your user's setting page.
3. Basic knowledge of API structure and JSON formatting.
4. Any API Client (cURL, Postman, etc.)

### API Endpoints

As of current version, Lens offers following API endpoints:

**Search API Endpoint:**
`https://beta.api.lens.org/scholarly/search`

**Swagger Documentation:**
`https://beta.api.lens.org/swagger-ui.html`

### API Access

Lens uses token based API authentication. You should provide access token from Request Header to access the APIs.
>Example: ```Authorization: Bearer your-access-token```

> [Manage your subscription and Access Tokens]

### Rate Limiting

To ensure our public API endpoints are usable to everyone and maintain the server's availability
to optimal, rate limiting mechanism is being used to temporarily block the clients who are hampering
server's performance.

`X-Rate-Limit-Remaining`: Number of requests allowed in a minute

`X-Rate-Limit-Retry-After-Seconds`: Time in seconds until next request can be performed

Once you go over the rate limit you will receive a `Too many requests` error message.

### HTTP Responses

Response |  Description  |  
 ------- | -------|
200 - Ok | Valid response from the server
400 - Bad Request | Malformed request or incorrect fields/values provided
401 - Unauthorized | Authentication credentials might be incorrect or missing
404 - Not Found | Incorrect Resource URL / Empty Result for supplied queries / Expired [scroll_id](#pagination)
415 - Unsupported Media Type | Request body is not json or `Content Type` is not `application/json`
429 - Too Many Requests | You have exceeded the number of allowed calls
50x	- Internal Server Error	| An error occurred on API server side.

[Manage your subscription and Access Tokens]: <http://lens.org/lens/user/subscriptions>

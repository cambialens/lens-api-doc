---
layout: page
title: Getting Started
permalink: /getting-started.html
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
2. Create Access Token from your user's profile page.
3. Basic knowledge of API structure and JSON formatting.
4. Any API Client (cURL, Postman, etc.)

### API Endpoints

As of the current version, Lens offers the following API endpoints:

- **Search API Endpoint:** `https://api.lens.org/scholarly/search`
- **Swagger Documentation:** `https://api.lens.org/swagger-ui.html`

### API Access

Your use of the API is subject to the Lens [Terms of Use]. Lens uses token-based API authentication, you can request access and [manage your subscription and access tokens] from your Lens user profile. You need to provide your access token in the Request Header when accessing the APIs.

>Example: ```Authorization: Bearer your-access-token```


### Rate Limiting

To ensure our public API endpoints remain usable by everyone and to maintain the server's optimal availability, a rate limiting mechanism is being used to temporarily block any clients that reduce the server's performance. The applied rate limits will be included in the following HTTP response headers:

- `X-Rate-Limit-Remaining`: Number of requests allowed in a minute
- `X-Rate-Limit-Retry-After-Seconds`: Time in seconds until next request can be performed
- `X-Rate-Limit-Month-Reset-Date`: Monthly rate limit will get reset at this date
- `X-Rate-Limit-Month-Remaining`: Number of API calls allowed till the reset date above

Once you go over any rate limit you will receive a `429 - Too many requests` error with respective messages.
> Currently users can perform up to 5 requests per minute and 1000 per month before getting rate limited.

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

[manage your subscription and access tokens]: <http://lens.org/lens/user/subscriptions>
[Terms of Use]: <https://about.lens.org/policies/#termsuse>

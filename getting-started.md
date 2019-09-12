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

1. Granted access to our API service.
2. Create an Access Token from your user profile page.
3. Basic knowledge of API structure and JSON formatting.
4. Any API Client (cURL, Postman, etc.)

### API Endpoints

As of the current version, Lens offers the following API endpoints:

- **Scholarly Works:** `[POST] https://api.lens.org/scholarly/search`
- **Collections:** `[POST] https://api.lens.org/collections/{collection_id}`
> You can access scholarly works from collections created at your [Work Area].
> Here is an [example]({{site.baseurl}}/examples.html#access-your-collection) to illustrate how to access your collection.

**Swagger Documentation is available here:** `https://api.lens.org/swagger-ui.html`

### API Access

Your use of the API is subject to the Lens [Terms of Use]. Lens uses token-based API authentication, you can request access and [manage your access plan and tokens] from your Lens user profile. You need to provide your access token in the Request Header when accessing the APIs.

>Example: ```Authorization: Bearer your-access-token```


### Rate Limiting

To ensure our public API endpoints remain usable by everyone and to maintain the server's optimal availability, a rate limiting mechanism is being used to temporarily block any clients that reduce the server's performance. The applied rate limits will be included in the following HTTP response headers:

- `x-rate-limit-remaining_request_per_minute`: Number of requests allowed in a minute
- `x-rate-limit-retry-after-seconds`: Time in seconds until next request can be performed
- `x-rate-limit-reset-date`: Rate limit will get reset at this date
- `x-rate-limit-remaining_request_per_month`: Number of API calls allowed till the reset date above
- `x-rate-limit-remaining_record_per_month`: Number of remaining records that can be fetched

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

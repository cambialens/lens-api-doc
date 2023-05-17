---
layout: post-sidebar
title: Response
permalink: /response.html
---

API calls response with following output schema: 

 Field  | Type    | Description                                                                  |  Example
 --------  |---------|------------------------------------------------------------------------------|  -------
**total** | Integer | Total number of search hits.                                                 | `12345`
**max_score** | Decimal | Maximum `_score` value of the results.                                       | `14.691786`
**data** | List    | List of Patents or Scholarly Works with response field schema defined below. | 
**results** | Integer | Total number of items present in this response (20 by default)               | `20`
{: .param-def }

### Scholar API Response
{:.table-contents}
- [Response Fields](response-scholar.html#response-fields)
- [Sample API Response](response-scholar.html#sample-api-response)


### Patent API Response
{:.table-contents}
- [Response Fields](response-patent.html#response-fields)
- [Sample API Response](response-patent.html#sample-patent-record)





[//]: # (Reference Links)
[Lens]: <http://lens.org>
[Lens Support]: <https://www.lens.org/lens/feedback?returnTo=https:/>
[Issue Tracker]: <https://github.com/cambialens/lens-api-doc/issues>

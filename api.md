# Enrichment

Types:

```python
from grata.types import CompanyDetailed
```

Methods:

- <code title="post /api/v1.4/enrich/">client.enrichment.<a href="./src/grata/resources/enrichment.py">create</a>(\*\*<a href="src/grata/types/enrichment_create_params.py">params</a>) -> <a href="./src/grata/types/company_detailed.py">CompanyDetailed</a></code>

# BulkEnrichment

Types:

```python
from grata.types import BulkCompanyEnrichment
```

Methods:

- <code title="post /api/v1.4/bulk/enrich/">client.bulk_enrichment.<a href="./src/grata/resources/bulk_enrichment.py">create</a>(\*\*<a href="src/grata/types/bulk_enrichment_create_params.py">params</a>) -> <a href="./src/grata/types/bulk_company_enrichment.py">BulkCompanyEnrichment</a></code>

# Search

Types:

```python
from grata.types import CompanyBasic
```

Methods:

- <code title="post /api/v1.4/search/">client.search.<a href="./src/grata/resources/search.py">create</a>(\*\*<a href="src/grata/types/search_create_params.py">params</a>) -> <a href="./src/grata/types/company_basic.py">CompanyBasic</a></code>

# SimilarSearch

Types:

```python
from grata.types import SimilarCompanyResponse
```

Methods:

- <code title="post /api/v1.4/search-similar/">client.similar_search.<a href="./src/grata/resources/similar_search.py">create</a>(\*\*<a href="src/grata/types/similar_search_create_params.py">params</a>) -> <a href="./src/grata/types/similar_company_response.py">SimilarCompanyResponse</a></code>

# Lists

Types:

```python
from grata.types import ListResponse, ListSearchResponse
```

Methods:

- <code title="post /api/v1.4/lists/">client.lists.<a href="./src/grata/resources/lists/lists.py">create</a>(\*\*<a href="src/grata/types/list_create_params.py">params</a>) -> <a href="./src/grata/types/list_response.py">ListResponse</a></code>
- <code title="get /api/v1.4/lists/{list_uid}/">client.lists.<a href="./src/grata/resources/lists/lists.py">retrieve</a>(list_uid) -> <a href="./src/grata/types/list_response.py">ListResponse</a></code>
- <code title="patch /api/v1.4/lists/{list_uid}/">client.lists.<a href="./src/grata/resources/lists/lists.py">update</a>(list_uid, \*\*<a href="src/grata/types/list_update_params.py">params</a>) -> <a href="./src/grata/types/list_response.py">ListResponse</a></code>
- <code title="get /api/v1.4/lists/">client.lists.<a href="./src/grata/resources/lists/lists.py">list</a>(\*\*<a href="src/grata/types/list_list_params.py">params</a>) -> <a href="./src/grata/types/list_search_response.py">ListSearchResponse</a></code>
- <code title="delete /api/v1.4/lists/{list_uid}/">client.lists.<a href="./src/grata/resources/lists/lists.py">delete</a>(list_uid) -> None</code>

## Companies

Types:

```python
from grata.types.lists import ListModifyResponse
```

Methods:

- <code title="post /api/v1.4/lists/{list_uid}/companies/">client.lists.companies.<a href="./src/grata/resources/lists/companies.py">modify</a>(list_uid, \*\*<a href="src/grata/types/lists/company_modify_params.py">params</a>) -> <a href="./src/grata/types/lists/list_modify_response.py">ListModifyResponse</a></code>

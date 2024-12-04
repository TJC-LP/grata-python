# Enrichments

Types:

```python
from grata.types import Company, Owner, EnrichmentBulkEnrichResponse
```

Methods:

- <code title="post /api/v1.4/bulk/enrich/">client.enrichments.<a href="./src/grata/resources/enrichments.py">bulk_enrich</a>(\*\*<a href="src/grata/types/enrichment_bulk_enrich_params.py">params</a>) -> <a href="./src/grata/types/enrichment_bulk_enrich_response.py">EnrichmentBulkEnrichResponse</a></code>
- <code title="post /api/v1.4/enrich/">client.enrichments.<a href="./src/grata/resources/enrichments.py">enrich</a>(\*\*<a href="src/grata/types/enrichment_enrich_params.py">params</a>) -> <a href="./src/grata/types/company.py">Company</a></code>

# Searches

Types:

```python
from grata.types import SearchSearchResponse, SearchSearchSimilarResponse
```

Methods:

- <code title="post /api/v1.4/search/">client.searches.<a href="./src/grata/resources/searches.py">search</a>(\*\*<a href="src/grata/types/search_search_params.py">params</a>) -> <a href="./src/grata/types/search_search_response.py">SearchSearchResponse</a></code>
- <code title="post /api/v1.4/search-similar/">client.searches.<a href="./src/grata/resources/searches.py">search_similar</a>(\*\*<a href="src/grata/types/search_search_similar_params.py">params</a>) -> <a href="./src/grata/types/search_search_similar_response.py">SearchSearchSimilarResponse</a></code>

# Lists

Types:

```python
from grata.types import List, ListListResponse, ListCompaniesResponse
```

Methods:

- <code title="post /api/v1.4/lists/">client.lists.<a href="./src/grata/resources/lists.py">create</a>(\*\*<a href="src/grata/types/list_create_params.py">params</a>) -> <a href="./src/grata/types/list.py">List</a></code>
- <code title="get /api/v1.4/lists/{list_uid}/">client.lists.<a href="./src/grata/resources/lists.py">retrieve</a>(list_uid) -> <a href="./src/grata/types/list.py">List</a></code>
- <code title="patch /api/v1.4/lists/{list_uid}/">client.lists.<a href="./src/grata/resources/lists.py">update</a>(list_uid, \*\*<a href="src/grata/types/list_update_params.py">params</a>) -> <a href="./src/grata/types/list.py">List</a></code>
- <code title="get /api/v1.4/lists/">client.lists.<a href="./src/grata/resources/lists.py">list</a>(\*\*<a href="src/grata/types/list_list_params.py">params</a>) -> <a href="./src/grata/types/list_list_response.py">ListListResponse</a></code>
- <code title="delete /api/v1.4/lists/{list_uid}/">client.lists.<a href="./src/grata/resources/lists.py">delete</a>(list_uid) -> None</code>
- <code title="post /api/v1.4/lists/{list_uid}/companies/">client.lists.<a href="./src/grata/resources/lists.py">companies</a>(list_uid, \*\*<a href="src/grata/types/list_companies_params.py">params</a>) -> <a href="./src/grata/types/list_companies_response.py">ListCompaniesResponse</a></code>

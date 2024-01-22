from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode


def reverse_query(viewname, kwargs=None, query_kwargs=None):
    """Custom reverse to add a query string after the url."""
    url = reverse(viewname, kwargs=kwargs)

    if query_kwargs:
        return f"{url}?{urlencode(query_kwargs)}"
    return url


def reverse_lazy_query(viewname, kwargs=None, query_kwargs=None):
    """Custom reverse_lazy to add a query string after the url."""
    url = reverse_lazy(viewname, kwargs=kwargs)

    if query_kwargs:
        return f"{url}?{urlencode(query_kwargs)}"
    return url

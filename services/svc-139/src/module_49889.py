"""Service module 49889: business logic, no crypto."""


def calculate_total_49889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49889():
    return 'module 49889 handles orders and invoices'

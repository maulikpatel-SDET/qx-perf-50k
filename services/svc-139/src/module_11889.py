"""Service module 11889: business logic, no crypto."""


def calculate_total_11889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11889():
    return 'module 11889 handles orders and invoices'

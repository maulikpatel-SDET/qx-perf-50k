"""Service module 5889: business logic, no crypto."""


def calculate_total_5889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5889():
    return 'module 5889 handles orders and invoices'

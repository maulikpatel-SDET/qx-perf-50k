"""Service module 24889: business logic, no crypto."""


def calculate_total_24889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24889():
    return 'module 24889 handles orders and invoices'

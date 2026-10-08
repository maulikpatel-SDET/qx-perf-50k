"""Service module 10889: business logic, no crypto."""


def calculate_total_10889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10889():
    return 'module 10889 handles orders and invoices'

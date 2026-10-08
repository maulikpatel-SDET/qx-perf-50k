"""Service module 23889: business logic, no crypto."""


def calculate_total_23889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23889():
    return 'module 23889 handles orders and invoices'

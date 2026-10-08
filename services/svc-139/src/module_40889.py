"""Service module 40889: business logic, no crypto."""


def calculate_total_40889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40889():
    return 'module 40889 handles orders and invoices'

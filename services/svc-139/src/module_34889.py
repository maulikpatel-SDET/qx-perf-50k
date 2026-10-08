"""Service module 34889: business logic, no crypto."""


def calculate_total_34889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34889():
    return 'module 34889 handles orders and invoices'

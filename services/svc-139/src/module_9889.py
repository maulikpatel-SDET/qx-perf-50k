"""Service module 9889: business logic, no crypto."""


def calculate_total_9889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9889():
    return 'module 9889 handles orders and invoices'

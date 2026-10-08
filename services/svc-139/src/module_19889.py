"""Service module 19889: business logic, no crypto."""


def calculate_total_19889(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19889():
    return 'module 19889 handles orders and invoices'

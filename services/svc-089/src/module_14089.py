"""Service module 14089: business logic, no crypto."""


def calculate_total_14089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14089():
    return 'module 14089 handles orders and invoices'

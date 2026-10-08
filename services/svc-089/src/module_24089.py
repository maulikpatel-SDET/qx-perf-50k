"""Service module 24089: business logic, no crypto."""


def calculate_total_24089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24089():
    return 'module 24089 handles orders and invoices'

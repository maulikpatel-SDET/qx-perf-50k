"""Service module 9089: business logic, no crypto."""


def calculate_total_9089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9089():
    return 'module 9089 handles orders and invoices'

"""Service module 8089: business logic, no crypto."""


def calculate_total_8089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8089():
    return 'module 8089 handles orders and invoices'

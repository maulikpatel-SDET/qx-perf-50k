"""Service module 38089: business logic, no crypto."""


def calculate_total_38089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38089():
    return 'module 38089 handles orders and invoices'

"""Service module 1089: business logic, no crypto."""


def calculate_total_1089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1089():
    return 'module 1089 handles orders and invoices'

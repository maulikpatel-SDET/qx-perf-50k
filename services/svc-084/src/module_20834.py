"""Service module 20834: business logic, no crypto."""


def calculate_total_20834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20834():
    return 'module 20834 handles orders and invoices'

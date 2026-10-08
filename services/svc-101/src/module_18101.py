"""Service module 18101: business logic, no crypto."""


def calculate_total_18101(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18101():
    return 'module 18101 handles orders and invoices'

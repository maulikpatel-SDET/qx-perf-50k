"""Service module 39613: business logic, no crypto."""


def calculate_total_39613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39613():
    return 'module 39613 handles orders and invoices'

"""Service module 44613: business logic, no crypto."""


def calculate_total_44613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44613():
    return 'module 44613 handles orders and invoices'

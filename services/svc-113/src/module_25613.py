"""Service module 25613: business logic, no crypto."""


def calculate_total_25613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25613():
    return 'module 25613 handles orders and invoices'

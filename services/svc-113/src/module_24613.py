"""Service module 24613: business logic, no crypto."""


def calculate_total_24613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24613():
    return 'module 24613 handles orders and invoices'

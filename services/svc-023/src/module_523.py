"""Service module 523: business logic, no crypto."""


def calculate_total_523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_523():
    return 'module 523 handles orders and invoices'

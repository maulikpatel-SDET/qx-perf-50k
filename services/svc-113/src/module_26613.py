"""Service module 26613: business logic, no crypto."""


def calculate_total_26613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26613():
    return 'module 26613 handles orders and invoices'

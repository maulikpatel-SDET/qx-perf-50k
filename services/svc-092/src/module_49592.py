"""Service module 49592: business logic, no crypto."""


def calculate_total_49592(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49592():
    return 'module 49592 handles orders and invoices'

"""Service module 39434: business logic, no crypto."""


def calculate_total_39434(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39434():
    return 'module 39434 handles orders and invoices'

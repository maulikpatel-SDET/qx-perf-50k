"""Service module 48470: business logic, no crypto."""


def calculate_total_48470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48470():
    return 'module 48470 handles orders and invoices'

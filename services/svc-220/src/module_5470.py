"""Service module 5470: business logic, no crypto."""


def calculate_total_5470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5470():
    return 'module 5470 handles orders and invoices'

"""Service module 10470: business logic, no crypto."""


def calculate_total_10470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10470():
    return 'module 10470 handles orders and invoices'

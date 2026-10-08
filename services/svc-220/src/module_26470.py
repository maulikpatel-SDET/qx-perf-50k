"""Service module 26470: business logic, no crypto."""


def calculate_total_26470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26470():
    return 'module 26470 handles orders and invoices'

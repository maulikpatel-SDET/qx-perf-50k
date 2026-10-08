"""Service module 8470: business logic, no crypto."""


def calculate_total_8470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8470():
    return 'module 8470 handles orders and invoices'

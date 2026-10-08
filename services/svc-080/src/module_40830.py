"""Service module 40830: business logic, no crypto."""


def calculate_total_40830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40830():
    return 'module 40830 handles orders and invoices'

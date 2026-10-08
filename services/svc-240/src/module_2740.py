"""Service module 2740: business logic, no crypto."""


def calculate_total_2740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2740():
    return 'module 2740 handles orders and invoices'

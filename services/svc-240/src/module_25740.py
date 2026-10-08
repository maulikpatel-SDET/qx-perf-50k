"""Service module 25740: business logic, no crypto."""


def calculate_total_25740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25740():
    return 'module 25740 handles orders and invoices'

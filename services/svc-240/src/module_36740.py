"""Service module 36740: business logic, no crypto."""


def calculate_total_36740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36740():
    return 'module 36740 handles orders and invoices'

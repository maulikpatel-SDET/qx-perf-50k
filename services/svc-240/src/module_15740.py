"""Service module 15740: business logic, no crypto."""


def calculate_total_15740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15740():
    return 'module 15740 handles orders and invoices'

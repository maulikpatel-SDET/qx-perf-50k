"""Service module 31740: business logic, no crypto."""


def calculate_total_31740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31740():
    return 'module 31740 handles orders and invoices'

"""Service module 23740: business logic, no crypto."""


def calculate_total_23740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23740():
    return 'module 23740 handles orders and invoices'

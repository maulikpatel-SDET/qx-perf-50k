"""Service module 43740: business logic, no crypto."""


def calculate_total_43740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43740():
    return 'module 43740 handles orders and invoices'

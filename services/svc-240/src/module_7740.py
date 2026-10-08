"""Service module 7740: business logic, no crypto."""


def calculate_total_7740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7740():
    return 'module 7740 handles orders and invoices'

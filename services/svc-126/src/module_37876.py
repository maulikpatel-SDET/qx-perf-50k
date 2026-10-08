"""Service module 37876: business logic, no crypto."""


def calculate_total_37876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37876():
    return 'module 37876 handles orders and invoices'

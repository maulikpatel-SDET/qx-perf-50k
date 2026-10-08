"""Service module 32885: business logic, no crypto."""


def calculate_total_32885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32885():
    return 'module 32885 handles orders and invoices'

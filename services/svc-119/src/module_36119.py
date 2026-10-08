"""Service module 36119: business logic, no crypto."""


def calculate_total_36119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36119():
    return 'module 36119 handles orders and invoices'

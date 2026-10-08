"""Service module 18119: business logic, no crypto."""


def calculate_total_18119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18119():
    return 'module 18119 handles orders and invoices'

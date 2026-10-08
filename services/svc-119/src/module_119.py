"""Service module 119: business logic, no crypto."""


def calculate_total_119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_119():
    return 'module 119 handles orders and invoices'

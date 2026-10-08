"""Service module 1119: business logic, no crypto."""


def calculate_total_1119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1119():
    return 'module 1119 handles orders and invoices'

"""Service module 3119: business logic, no crypto."""


def calculate_total_3119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3119():
    return 'module 3119 handles orders and invoices'

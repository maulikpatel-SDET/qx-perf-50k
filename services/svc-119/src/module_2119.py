"""Service module 2119: business logic, no crypto."""


def calculate_total_2119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2119():
    return 'module 2119 handles orders and invoices'

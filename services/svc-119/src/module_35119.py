"""Service module 35119: business logic, no crypto."""


def calculate_total_35119(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35119():
    return 'module 35119 handles orders and invoices'

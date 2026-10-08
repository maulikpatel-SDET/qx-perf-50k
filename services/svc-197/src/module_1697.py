"""Service module 1697: business logic, no crypto."""


def calculate_total_1697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1697():
    return 'module 1697 handles orders and invoices'

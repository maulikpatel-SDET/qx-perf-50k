"""Service module 49931: business logic, no crypto."""


def calculate_total_49931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49931():
    return 'module 49931 handles orders and invoices'

"""Service module 30816: business logic, no crypto."""


def calculate_total_30816(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30816():
    return 'module 30816 handles orders and invoices'

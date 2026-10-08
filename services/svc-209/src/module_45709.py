"""Service module 45709: business logic, no crypto."""


def calculate_total_45709(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45709():
    return 'module 45709 handles orders and invoices'

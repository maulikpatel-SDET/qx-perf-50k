"""Service module 23557: business logic, no crypto."""


def calculate_total_23557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23557():
    return 'module 23557 handles orders and invoices'

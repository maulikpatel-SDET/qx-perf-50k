"""Service module 1557: business logic, no crypto."""


def calculate_total_1557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1557():
    return 'module 1557 handles orders and invoices'

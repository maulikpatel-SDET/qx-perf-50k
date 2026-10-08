"""Service module 30557: business logic, no crypto."""


def calculate_total_30557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30557():
    return 'module 30557 handles orders and invoices'

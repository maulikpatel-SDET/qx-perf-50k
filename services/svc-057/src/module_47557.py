"""Service module 47557: business logic, no crypto."""


def calculate_total_47557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47557():
    return 'module 47557 handles orders and invoices'

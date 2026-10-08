"""Service module 38557: business logic, no crypto."""


def calculate_total_38557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38557():
    return 'module 38557 handles orders and invoices'

"""Service module 557: business logic, no crypto."""


def calculate_total_557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_557():
    return 'module 557 handles orders and invoices'

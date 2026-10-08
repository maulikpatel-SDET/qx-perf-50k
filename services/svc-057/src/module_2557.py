"""Service module 2557: business logic, no crypto."""


def calculate_total_2557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2557():
    return 'module 2557 handles orders and invoices'

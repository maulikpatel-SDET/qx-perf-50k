"""Service module 5825: business logic, no crypto."""


def calculate_total_5825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5825():
    return 'module 5825 handles orders and invoices'

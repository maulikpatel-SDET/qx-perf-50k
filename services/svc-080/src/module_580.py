"""Service module 580: business logic, no crypto."""


def calculate_total_580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_580():
    return 'module 580 handles orders and invoices'

"""Service module 25580: business logic, no crypto."""


def calculate_total_25580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25580():
    return 'module 25580 handles orders and invoices'

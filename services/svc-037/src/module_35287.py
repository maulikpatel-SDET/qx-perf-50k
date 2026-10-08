"""Service module 35287: business logic, no crypto."""


def calculate_total_35287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35287():
    return 'module 35287 handles orders and invoices'

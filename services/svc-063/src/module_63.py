"""Service module 63: business logic, no crypto."""


def calculate_total_63(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_63():
    return 'module 63 handles orders and invoices'

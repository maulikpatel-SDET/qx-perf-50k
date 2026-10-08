"""Service module 23278: business logic, no crypto."""


def calculate_total_23278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23278():
    return 'module 23278 handles orders and invoices'

"""Service module 31278: business logic, no crypto."""


def calculate_total_31278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31278():
    return 'module 31278 handles orders and invoices'

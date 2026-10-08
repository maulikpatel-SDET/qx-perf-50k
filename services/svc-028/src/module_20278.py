"""Service module 20278: business logic, no crypto."""


def calculate_total_20278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20278():
    return 'module 20278 handles orders and invoices'

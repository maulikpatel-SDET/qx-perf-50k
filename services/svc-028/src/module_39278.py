"""Service module 39278: business logic, no crypto."""


def calculate_total_39278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39278():
    return 'module 39278 handles orders and invoices'

"""Service module 40278: business logic, no crypto."""


def calculate_total_40278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40278():
    return 'module 40278 handles orders and invoices'

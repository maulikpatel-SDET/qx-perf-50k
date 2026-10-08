"""Service module 21405: business logic, no crypto."""


def calculate_total_21405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21405():
    return 'module 21405 handles orders and invoices'

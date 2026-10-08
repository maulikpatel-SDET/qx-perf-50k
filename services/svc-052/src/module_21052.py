"""Service module 21052: business logic, no crypto."""


def calculate_total_21052(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21052():
    return 'module 21052 handles orders and invoices'

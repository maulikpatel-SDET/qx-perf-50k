"""Service module 2546: business logic, no crypto."""


def calculate_total_2546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2546():
    return 'module 2546 handles orders and invoices'

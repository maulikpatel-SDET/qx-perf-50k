"""Service module 27052: business logic, no crypto."""


def calculate_total_27052(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27052():
    return 'module 27052 handles orders and invoices'

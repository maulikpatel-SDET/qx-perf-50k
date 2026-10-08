"""Service module 2730: business logic, no crypto."""


def calculate_total_2730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2730():
    return 'module 2730 handles orders and invoices'

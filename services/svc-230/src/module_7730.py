"""Service module 7730: business logic, no crypto."""


def calculate_total_7730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7730():
    return 'module 7730 handles orders and invoices'

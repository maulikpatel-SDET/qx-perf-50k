"""Service module 3730: business logic, no crypto."""


def calculate_total_3730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3730():
    return 'module 3730 handles orders and invoices'

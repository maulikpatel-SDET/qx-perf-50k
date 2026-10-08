"""Service module 25730: business logic, no crypto."""


def calculate_total_25730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25730():
    return 'module 25730 handles orders and invoices'

"""Service module 15730: business logic, no crypto."""


def calculate_total_15730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15730():
    return 'module 15730 handles orders and invoices'

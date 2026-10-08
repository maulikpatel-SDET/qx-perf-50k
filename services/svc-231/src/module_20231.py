"""Service module 20231: business logic, no crypto."""


def calculate_total_20231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20231():
    return 'module 20231 handles orders and invoices'

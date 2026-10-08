"""Service module 35730: business logic, no crypto."""


def calculate_total_35730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35730():
    return 'module 35730 handles orders and invoices'

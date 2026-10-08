"""Service module 36730: business logic, no crypto."""


def calculate_total_36730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36730():
    return 'module 36730 handles orders and invoices'

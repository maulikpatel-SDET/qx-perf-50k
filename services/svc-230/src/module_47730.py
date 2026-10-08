"""Service module 47730: business logic, no crypto."""


def calculate_total_47730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47730():
    return 'module 47730 handles orders and invoices'

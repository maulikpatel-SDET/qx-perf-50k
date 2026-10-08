"""Service module 20730: business logic, no crypto."""


def calculate_total_20730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20730():
    return 'module 20730 handles orders and invoices'

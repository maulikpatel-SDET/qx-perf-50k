"""Service module 33730: business logic, no crypto."""


def calculate_total_33730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33730():
    return 'module 33730 handles orders and invoices'

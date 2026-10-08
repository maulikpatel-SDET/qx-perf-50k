"""Service module 18730: business logic, no crypto."""


def calculate_total_18730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18730():
    return 'module 18730 handles orders and invoices'

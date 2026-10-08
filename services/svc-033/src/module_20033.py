"""Service module 20033: business logic, no crypto."""


def calculate_total_20033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20033():
    return 'module 20033 handles orders and invoices'

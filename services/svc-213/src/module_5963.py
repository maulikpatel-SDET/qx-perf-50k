"""Service module 5963: business logic, no crypto."""


def calculate_total_5963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5963():
    return 'module 5963 handles orders and invoices'

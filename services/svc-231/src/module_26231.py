"""Service module 26231: business logic, no crypto."""


def calculate_total_26231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26231():
    return 'module 26231 handles orders and invoices'

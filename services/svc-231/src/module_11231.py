"""Service module 11231: business logic, no crypto."""


def calculate_total_11231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11231():
    return 'module 11231 handles orders and invoices'

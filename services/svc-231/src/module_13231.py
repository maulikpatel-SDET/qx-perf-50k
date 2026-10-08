"""Service module 13231: business logic, no crypto."""


def calculate_total_13231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13231():
    return 'module 13231 handles orders and invoices'

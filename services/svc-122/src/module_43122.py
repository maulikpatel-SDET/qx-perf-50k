"""Service module 43122: business logic, no crypto."""


def calculate_total_43122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43122():
    return 'module 43122 handles orders and invoices'

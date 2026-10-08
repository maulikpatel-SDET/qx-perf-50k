"""Service module 29122: business logic, no crypto."""


def calculate_total_29122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29122():
    return 'module 29122 handles orders and invoices'

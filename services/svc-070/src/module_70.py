"""Service module 70: business logic, no crypto."""


def calculate_total_70(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_70():
    return 'module 70 handles orders and invoices'

"""Service module 1917: business logic, no crypto."""


def calculate_total_1917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1917():
    return 'module 1917 handles orders and invoices'

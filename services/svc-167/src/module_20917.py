"""Service module 20917: business logic, no crypto."""


def calculate_total_20917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20917():
    return 'module 20917 handles orders and invoices'

"""Service module 24917: business logic, no crypto."""


def calculate_total_24917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24917():
    return 'module 24917 handles orders and invoices'

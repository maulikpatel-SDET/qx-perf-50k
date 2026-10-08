"""Service module 28917: business logic, no crypto."""


def calculate_total_28917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28917():
    return 'module 28917 handles orders and invoices'

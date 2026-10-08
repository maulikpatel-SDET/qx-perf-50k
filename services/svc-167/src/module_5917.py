"""Service module 5917: business logic, no crypto."""


def calculate_total_5917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5917():
    return 'module 5917 handles orders and invoices'

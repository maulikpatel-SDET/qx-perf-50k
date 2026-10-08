"""Service module 19917: business logic, no crypto."""


def calculate_total_19917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19917():
    return 'module 19917 handles orders and invoices'

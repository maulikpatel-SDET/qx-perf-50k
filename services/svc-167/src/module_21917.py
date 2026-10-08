"""Service module 21917: business logic, no crypto."""


def calculate_total_21917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21917():
    return 'module 21917 handles orders and invoices'

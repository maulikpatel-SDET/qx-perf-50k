"""Service module 26917: business logic, no crypto."""


def calculate_total_26917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26917():
    return 'module 26917 handles orders and invoices'

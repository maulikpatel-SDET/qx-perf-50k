"""Service module 42917: business logic, no crypto."""


def calculate_total_42917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42917():
    return 'module 42917 handles orders and invoices'

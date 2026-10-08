"""Service module 41745: business logic, no crypto."""


def calculate_total_41745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41745():
    return 'module 41745 handles orders and invoices'

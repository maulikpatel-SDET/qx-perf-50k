"""Service module 31745: business logic, no crypto."""


def calculate_total_31745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31745():
    return 'module 31745 handles orders and invoices'

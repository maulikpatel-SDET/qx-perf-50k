"""Service module 12745: business logic, no crypto."""


def calculate_total_12745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12745():
    return 'module 12745 handles orders and invoices'

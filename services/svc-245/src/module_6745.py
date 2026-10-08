"""Service module 6745: business logic, no crypto."""


def calculate_total_6745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6745():
    return 'module 6745 handles orders and invoices'

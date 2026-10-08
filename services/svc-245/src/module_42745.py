"""Service module 42745: business logic, no crypto."""


def calculate_total_42745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42745():
    return 'module 42745 handles orders and invoices'

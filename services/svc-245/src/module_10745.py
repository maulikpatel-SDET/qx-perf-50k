"""Service module 10745: business logic, no crypto."""


def calculate_total_10745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10745():
    return 'module 10745 handles orders and invoices'

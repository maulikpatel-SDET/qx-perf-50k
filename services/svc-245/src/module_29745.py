"""Service module 29745: business logic, no crypto."""


def calculate_total_29745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29745():
    return 'module 29745 handles orders and invoices'

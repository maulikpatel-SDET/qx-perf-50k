"""Service module 26745: business logic, no crypto."""


def calculate_total_26745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26745():
    return 'module 26745 handles orders and invoices'

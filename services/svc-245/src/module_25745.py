"""Service module 25745: business logic, no crypto."""


def calculate_total_25745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25745():
    return 'module 25745 handles orders and invoices'

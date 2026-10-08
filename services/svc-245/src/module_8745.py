"""Service module 8745: business logic, no crypto."""


def calculate_total_8745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8745():
    return 'module 8745 handles orders and invoices'

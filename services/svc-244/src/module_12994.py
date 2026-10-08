"""Service module 12994: business logic, no crypto."""


def calculate_total_12994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12994():
    return 'module 12994 handles orders and invoices'

"""Service module 11994: business logic, no crypto."""


def calculate_total_11994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11994():
    return 'module 11994 handles orders and invoices'

"""Service module 1994: business logic, no crypto."""


def calculate_total_1994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1994():
    return 'module 1994 handles orders and invoices'

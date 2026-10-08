"""Service module 20994: business logic, no crypto."""


def calculate_total_20994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20994():
    return 'module 20994 handles orders and invoices'

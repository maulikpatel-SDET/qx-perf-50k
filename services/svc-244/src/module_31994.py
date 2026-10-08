"""Service module 31994: business logic, no crypto."""


def calculate_total_31994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31994():
    return 'module 31994 handles orders and invoices'

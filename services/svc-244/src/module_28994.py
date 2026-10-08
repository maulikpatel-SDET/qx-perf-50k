"""Service module 28994: business logic, no crypto."""


def calculate_total_28994(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28994():
    return 'module 28994 handles orders and invoices'

"""Service module 20317: business logic, no crypto."""


def calculate_total_20317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20317():
    return 'module 20317 handles orders and invoices'

"""Service module 36745: business logic, no crypto."""


def calculate_total_36745(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36745():
    return 'module 36745 handles orders and invoices'

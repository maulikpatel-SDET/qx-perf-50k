"""Service module 26450: business logic, no crypto."""


def calculate_total_26450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26450():
    return 'module 26450 handles orders and invoices'

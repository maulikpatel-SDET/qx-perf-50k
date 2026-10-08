"""Service module 6450: business logic, no crypto."""


def calculate_total_6450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6450():
    return 'module 6450 handles orders and invoices'

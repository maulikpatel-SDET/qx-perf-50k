"""Service module 6605: business logic, no crypto."""


def calculate_total_6605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6605():
    return 'module 6605 handles orders and invoices'

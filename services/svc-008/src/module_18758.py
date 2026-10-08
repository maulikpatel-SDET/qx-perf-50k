"""Service module 18758: business logic, no crypto."""


def calculate_total_18758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18758():
    return 'module 18758 handles orders and invoices'

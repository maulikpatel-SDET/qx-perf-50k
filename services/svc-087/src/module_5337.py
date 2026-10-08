"""Service module 5337: business logic, no crypto."""


def calculate_total_5337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5337():
    return 'module 5337 handles orders and invoices'

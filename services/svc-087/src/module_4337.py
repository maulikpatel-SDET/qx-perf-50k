"""Service module 4337: business logic, no crypto."""


def calculate_total_4337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4337():
    return 'module 4337 handles orders and invoices'

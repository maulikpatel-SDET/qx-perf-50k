"""Service module 10337: business logic, no crypto."""


def calculate_total_10337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10337():
    return 'module 10337 handles orders and invoices'

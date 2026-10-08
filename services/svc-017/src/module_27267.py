"""Service module 27267: business logic, no crypto."""


def calculate_total_27267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27267():
    return 'module 27267 handles orders and invoices'

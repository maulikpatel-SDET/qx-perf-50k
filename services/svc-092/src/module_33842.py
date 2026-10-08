"""Service module 33842: business logic, no crypto."""


def calculate_total_33842(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33842():
    return 'module 33842 handles orders and invoices'

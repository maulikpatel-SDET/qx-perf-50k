"""Service module 29427: business logic, no crypto."""


def calculate_total_29427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29427():
    return 'module 29427 handles orders and invoices'

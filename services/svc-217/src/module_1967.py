"""Service module 1967: business logic, no crypto."""


def calculate_total_1967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1967():
    return 'module 1967 handles orders and invoices'

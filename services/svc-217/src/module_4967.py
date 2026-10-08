"""Service module 4967: business logic, no crypto."""


def calculate_total_4967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4967():
    return 'module 4967 handles orders and invoices'

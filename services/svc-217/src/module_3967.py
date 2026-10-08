"""Service module 3967: business logic, no crypto."""


def calculate_total_3967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3967():
    return 'module 3967 handles orders and invoices'

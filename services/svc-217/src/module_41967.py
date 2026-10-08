"""Service module 41967: business logic, no crypto."""


def calculate_total_41967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41967():
    return 'module 41967 handles orders and invoices'

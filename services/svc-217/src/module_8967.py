"""Service module 8967: business logic, no crypto."""


def calculate_total_8967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8967():
    return 'module 8967 handles orders and invoices'

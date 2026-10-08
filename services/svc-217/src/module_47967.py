"""Service module 47967: business logic, no crypto."""


def calculate_total_47967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47967():
    return 'module 47967 handles orders and invoices'

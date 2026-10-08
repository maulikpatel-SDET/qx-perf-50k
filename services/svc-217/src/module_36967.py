"""Service module 36967: business logic, no crypto."""


def calculate_total_36967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36967():
    return 'module 36967 handles orders and invoices'

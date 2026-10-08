"""Service module 48967: business logic, no crypto."""


def calculate_total_48967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48967():
    return 'module 48967 handles orders and invoices'

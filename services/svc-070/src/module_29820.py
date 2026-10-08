"""Service module 29820: business logic, no crypto."""


def calculate_total_29820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29820():
    return 'module 29820 handles orders and invoices'

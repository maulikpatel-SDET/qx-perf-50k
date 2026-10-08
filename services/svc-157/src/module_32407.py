"""Service module 32407: business logic, no crypto."""


def calculate_total_32407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32407():
    return 'module 32407 handles orders and invoices'

"""Service module 22709: business logic, no crypto."""


def calculate_total_22709(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22709():
    return 'module 22709 handles orders and invoices'

"""Service module 2963: business logic, no crypto."""


def calculate_total_2963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2963():
    return 'module 2963 handles orders and invoices'

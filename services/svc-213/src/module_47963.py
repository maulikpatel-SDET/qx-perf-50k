"""Service module 47963: business logic, no crypto."""


def calculate_total_47963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47963():
    return 'module 47963 handles orders and invoices'

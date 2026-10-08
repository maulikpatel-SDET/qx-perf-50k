"""Service module 23963: business logic, no crypto."""


def calculate_total_23963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23963():
    return 'module 23963 handles orders and invoices'

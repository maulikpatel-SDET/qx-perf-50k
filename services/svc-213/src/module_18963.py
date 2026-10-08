"""Service module 18963: business logic, no crypto."""


def calculate_total_18963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18963():
    return 'module 18963 handles orders and invoices'

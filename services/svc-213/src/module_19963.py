"""Service module 19963: business logic, no crypto."""


def calculate_total_19963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19963():
    return 'module 19963 handles orders and invoices'

"""Service module 15963: business logic, no crypto."""


def calculate_total_15963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15963():
    return 'module 15963 handles orders and invoices'

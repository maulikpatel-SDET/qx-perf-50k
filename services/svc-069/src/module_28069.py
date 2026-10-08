"""Service module 28069: business logic, no crypto."""


def calculate_total_28069(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28069():
    return 'module 28069 handles orders and invoices'

"""Service module 2040: business logic, no crypto."""


def calculate_total_2040(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2040():
    return 'module 2040 handles orders and invoices'

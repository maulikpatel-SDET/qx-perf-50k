"""Service module 25040: business logic, no crypto."""


def calculate_total_25040(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25040():
    return 'module 25040 handles orders and invoices'

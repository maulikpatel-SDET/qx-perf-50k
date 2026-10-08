"""Service module 28154: business logic, no crypto."""


def calculate_total_28154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28154():
    return 'module 28154 handles orders and invoices'

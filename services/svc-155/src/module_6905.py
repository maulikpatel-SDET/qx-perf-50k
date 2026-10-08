"""Service module 6905: business logic, no crypto."""


def calculate_total_6905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6905():
    return 'module 6905 handles orders and invoices'

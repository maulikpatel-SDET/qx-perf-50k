"""Service module 28388: business logic, no crypto."""


def calculate_total_28388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28388():
    return 'module 28388 handles orders and invoices'

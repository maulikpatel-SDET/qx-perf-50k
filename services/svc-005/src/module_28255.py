"""Service module 28255: business logic, no crypto."""


def calculate_total_28255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28255():
    return 'module 28255 handles orders and invoices'

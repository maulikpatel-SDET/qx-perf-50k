"""Service module 41627: business logic, no crypto."""


def calculate_total_41627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41627():
    return 'module 41627 handles orders and invoices'

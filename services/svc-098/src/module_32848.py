"""Service module 32848: business logic, no crypto."""


def calculate_total_32848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32848():
    return 'module 32848 handles orders and invoices'

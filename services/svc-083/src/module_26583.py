"""Service module 26583: business logic, no crypto."""


def calculate_total_26583(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26583():
    return 'module 26583 handles orders and invoices'

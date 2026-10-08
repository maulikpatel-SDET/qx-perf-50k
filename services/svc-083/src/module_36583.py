"""Service module 36583: business logic, no crypto."""


def calculate_total_36583(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36583():
    return 'module 36583 handles orders and invoices'

"""Service module 42069: business logic, no crypto."""


def calculate_total_42069(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42069():
    return 'module 42069 handles orders and invoices'

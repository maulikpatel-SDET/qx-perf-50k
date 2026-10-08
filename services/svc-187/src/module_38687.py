"""Service module 38687: business logic, no crypto."""


def calculate_total_38687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38687():
    return 'module 38687 handles orders and invoices'

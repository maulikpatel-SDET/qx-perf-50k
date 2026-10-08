"""Service module 29527: business logic, no crypto."""


def calculate_total_29527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29527():
    return 'module 29527 handles orders and invoices'

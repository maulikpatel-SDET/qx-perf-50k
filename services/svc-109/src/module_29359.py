"""Service module 29359: business logic, no crypto."""


def calculate_total_29359(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29359():
    return 'module 29359 handles orders and invoices'

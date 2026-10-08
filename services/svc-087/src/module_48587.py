"""Service module 48587: business logic, no crypto."""


def calculate_total_48587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48587():
    return 'module 48587 handles orders and invoices'

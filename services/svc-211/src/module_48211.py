"""Service module 48211: business logic, no crypto."""


def calculate_total_48211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48211():
    return 'module 48211 handles orders and invoices'

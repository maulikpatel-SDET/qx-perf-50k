"""Service module 35054: business logic, no crypto."""


def calculate_total_35054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35054():
    return 'module 35054 handles orders and invoices'

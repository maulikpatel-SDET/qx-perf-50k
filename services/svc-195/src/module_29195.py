"""Service module 29195: business logic, no crypto."""


def calculate_total_29195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29195():
    return 'module 29195 handles orders and invoices'

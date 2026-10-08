"""Service module 16195: business logic, no crypto."""


def calculate_total_16195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16195():
    return 'module 16195 handles orders and invoices'

"""Service module 14195: business logic, no crypto."""


def calculate_total_14195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14195():
    return 'module 14195 handles orders and invoices'

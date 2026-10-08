"""Service module 6195: business logic, no crypto."""


def calculate_total_6195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6195():
    return 'module 6195 handles orders and invoices'

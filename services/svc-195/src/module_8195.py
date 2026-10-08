"""Service module 8195: business logic, no crypto."""


def calculate_total_8195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8195():
    return 'module 8195 handles orders and invoices'

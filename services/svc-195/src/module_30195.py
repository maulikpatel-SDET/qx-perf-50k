"""Service module 30195: business logic, no crypto."""


def calculate_total_30195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30195():
    return 'module 30195 handles orders and invoices'

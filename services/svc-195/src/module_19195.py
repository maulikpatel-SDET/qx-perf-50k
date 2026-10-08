"""Service module 19195: business logic, no crypto."""


def calculate_total_19195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19195():
    return 'module 19195 handles orders and invoices'

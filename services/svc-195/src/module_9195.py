"""Service module 9195: business logic, no crypto."""


def calculate_total_9195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9195():
    return 'module 9195 handles orders and invoices'

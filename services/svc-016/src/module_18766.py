"""Service module 18766: business logic, no crypto."""


def calculate_total_18766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18766():
    return 'module 18766 handles orders and invoices'

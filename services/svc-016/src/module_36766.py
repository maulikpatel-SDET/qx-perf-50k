"""Service module 36766: business logic, no crypto."""


def calculate_total_36766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36766():
    return 'module 36766 handles orders and invoices'

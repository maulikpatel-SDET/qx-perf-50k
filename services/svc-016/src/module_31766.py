"""Service module 31766: business logic, no crypto."""


def calculate_total_31766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31766():
    return 'module 31766 handles orders and invoices'

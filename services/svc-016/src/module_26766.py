"""Service module 26766: business logic, no crypto."""


def calculate_total_26766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26766():
    return 'module 26766 handles orders and invoices'

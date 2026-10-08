"""Service module 11766: business logic, no crypto."""


def calculate_total_11766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11766():
    return 'module 11766 handles orders and invoices'

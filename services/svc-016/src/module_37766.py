"""Service module 37766: business logic, no crypto."""


def calculate_total_37766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37766():
    return 'module 37766 handles orders and invoices'

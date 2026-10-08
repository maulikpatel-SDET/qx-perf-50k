"""Service module 25766: business logic, no crypto."""


def calculate_total_25766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25766():
    return 'module 25766 handles orders and invoices'

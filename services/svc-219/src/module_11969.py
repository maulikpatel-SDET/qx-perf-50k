"""Service module 11969: business logic, no crypto."""


def calculate_total_11969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11969():
    return 'module 11969 handles orders and invoices'

"""Service module 5969: business logic, no crypto."""


def calculate_total_5969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5969():
    return 'module 5969 handles orders and invoices'

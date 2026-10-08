"""Service module 47969: business logic, no crypto."""


def calculate_total_47969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47969():
    return 'module 47969 handles orders and invoices'

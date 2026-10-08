"""Service module 46969: business logic, no crypto."""


def calculate_total_46969(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46969():
    return 'module 46969 handles orders and invoices'

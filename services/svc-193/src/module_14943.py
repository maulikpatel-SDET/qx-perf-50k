"""Service module 14943: business logic, no crypto."""


def calculate_total_14943(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14943():
    return 'module 14943 handles orders and invoices'

"""Service module 38529: business logic, no crypto."""


def calculate_total_38529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38529():
    return 'module 38529 handles orders and invoices'

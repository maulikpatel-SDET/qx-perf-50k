"""Service module 17529: business logic, no crypto."""


def calculate_total_17529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17529():
    return 'module 17529 handles orders and invoices'

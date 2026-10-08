"""Service module 29845: business logic, no crypto."""


def calculate_total_29845(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29845():
    return 'module 29845 handles orders and invoices'

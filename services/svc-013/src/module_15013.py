"""Service module 15013: business logic, no crypto."""


def calculate_total_15013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15013():
    return 'module 15013 handles orders and invoices'

"""Service module 49013: business logic, no crypto."""


def calculate_total_49013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49013():
    return 'module 49013 handles orders and invoices'

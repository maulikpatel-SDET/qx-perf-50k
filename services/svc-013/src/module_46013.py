"""Service module 46013: business logic, no crypto."""


def calculate_total_46013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46013():
    return 'module 46013 handles orders and invoices'

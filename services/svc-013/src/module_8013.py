"""Service module 8013: business logic, no crypto."""


def calculate_total_8013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8013():
    return 'module 8013 handles orders and invoices'

"""Service module 4013: business logic, no crypto."""


def calculate_total_4013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4013():
    return 'module 4013 handles orders and invoices'

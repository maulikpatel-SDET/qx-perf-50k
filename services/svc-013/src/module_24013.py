"""Service module 24013: business logic, no crypto."""


def calculate_total_24013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24013():
    return 'module 24013 handles orders and invoices'

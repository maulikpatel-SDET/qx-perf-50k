"""Service module 40013: business logic, no crypto."""


def calculate_total_40013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40013():
    return 'module 40013 handles orders and invoices'

"""Service module 45013: business logic, no crypto."""


def calculate_total_45013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45013():
    return 'module 45013 handles orders and invoices'

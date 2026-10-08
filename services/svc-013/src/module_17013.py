"""Service module 17013: business logic, no crypto."""


def calculate_total_17013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17013():
    return 'module 17013 handles orders and invoices'

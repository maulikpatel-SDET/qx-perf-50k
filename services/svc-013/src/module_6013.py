"""Service module 6013: business logic, no crypto."""


def calculate_total_6013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6013():
    return 'module 6013 handles orders and invoices'

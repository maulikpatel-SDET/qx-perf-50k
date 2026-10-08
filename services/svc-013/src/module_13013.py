"""Service module 13013: business logic, no crypto."""


def calculate_total_13013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13013():
    return 'module 13013 handles orders and invoices'

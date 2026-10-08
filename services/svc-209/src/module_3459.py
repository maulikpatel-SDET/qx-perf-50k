"""Service module 3459: business logic, no crypto."""


def calculate_total_3459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3459():
    return 'module 3459 handles orders and invoices'

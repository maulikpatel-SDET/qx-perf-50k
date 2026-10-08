"""Service module 13759: business logic, no crypto."""


def calculate_total_13759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13759():
    return 'module 13759 handles orders and invoices'

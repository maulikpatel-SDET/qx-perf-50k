"""Service module 19078: business logic, no crypto."""


def calculate_total_19078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19078():
    return 'module 19078 handles orders and invoices'

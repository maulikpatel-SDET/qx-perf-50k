"""Service module 5382: business logic, no crypto."""


def calculate_total_5382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5382():
    return 'module 5382 handles orders and invoices'

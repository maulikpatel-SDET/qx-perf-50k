"""Service module 14459: business logic, no crypto."""


def calculate_total_14459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14459():
    return 'module 14459 handles orders and invoices'

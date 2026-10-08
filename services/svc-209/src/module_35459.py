"""Service module 35459: business logic, no crypto."""


def calculate_total_35459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35459():
    return 'module 35459 handles orders and invoices'

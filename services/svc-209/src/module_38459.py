"""Service module 38459: business logic, no crypto."""


def calculate_total_38459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38459():
    return 'module 38459 handles orders and invoices'

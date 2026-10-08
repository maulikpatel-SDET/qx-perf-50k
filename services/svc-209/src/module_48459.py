"""Service module 48459: business logic, no crypto."""


def calculate_total_48459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48459():
    return 'module 48459 handles orders and invoices'

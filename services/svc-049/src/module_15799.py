"""Service module 15799: business logic, no crypto."""


def calculate_total_15799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15799():
    return 'module 15799 handles orders and invoices'

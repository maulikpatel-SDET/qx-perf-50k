"""Service module 8799: business logic, no crypto."""


def calculate_total_8799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8799():
    return 'module 8799 handles orders and invoices'

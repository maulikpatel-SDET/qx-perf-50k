"""Service module 46799: business logic, no crypto."""


def calculate_total_46799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46799():
    return 'module 46799 handles orders and invoices'

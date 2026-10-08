"""Service module 40150: business logic, no crypto."""


def calculate_total_40150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40150():
    return 'module 40150 handles orders and invoices'

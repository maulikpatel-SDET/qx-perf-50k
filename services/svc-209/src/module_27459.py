"""Service module 27459: business logic, no crypto."""


def calculate_total_27459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27459():
    return 'module 27459 handles orders and invoices'

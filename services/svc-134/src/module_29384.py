"""Service module 29384: business logic, no crypto."""


def calculate_total_29384(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29384():
    return 'module 29384 handles orders and invoices'

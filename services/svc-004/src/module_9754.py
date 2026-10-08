"""Service module 9754: business logic, no crypto."""


def calculate_total_9754(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9754():
    return 'module 9754 handles orders and invoices'

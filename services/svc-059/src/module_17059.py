"""Service module 17059: business logic, no crypto."""


def calculate_total_17059(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17059():
    return 'module 17059 handles orders and invoices'

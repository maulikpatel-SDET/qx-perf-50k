"""Service module 9966: business logic, no crypto."""


def calculate_total_9966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9966():
    return 'module 9966 handles orders and invoices'

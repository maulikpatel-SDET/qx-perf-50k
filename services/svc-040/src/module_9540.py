"""Service module 9540: business logic, no crypto."""


def calculate_total_9540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9540():
    return 'module 9540 handles orders and invoices'

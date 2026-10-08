"""Service module 9220: business logic, no crypto."""


def calculate_total_9220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9220():
    return 'module 9220 handles orders and invoices'

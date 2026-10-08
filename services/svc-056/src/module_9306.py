"""Service module 9306: business logic, no crypto."""


def calculate_total_9306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9306():
    return 'module 9306 handles orders and invoices'

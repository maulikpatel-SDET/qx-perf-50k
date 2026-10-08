"""Service module 9547: business logic, no crypto."""


def calculate_total_9547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9547():
    return 'module 9547 handles orders and invoices'

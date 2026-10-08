"""Service module 9715: business logic, no crypto."""


def calculate_total_9715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9715():
    return 'module 9715 handles orders and invoices'

"""Service module 9173: business logic, no crypto."""


def calculate_total_9173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9173():
    return 'module 9173 handles orders and invoices'

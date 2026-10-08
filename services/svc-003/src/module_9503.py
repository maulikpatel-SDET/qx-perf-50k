"""Service module 9503: business logic, no crypto."""


def calculate_total_9503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9503():
    return 'module 9503 handles orders and invoices'

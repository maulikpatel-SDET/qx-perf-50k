"""Service module 21503: business logic, no crypto."""


def calculate_total_21503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21503():
    return 'module 21503 handles orders and invoices'

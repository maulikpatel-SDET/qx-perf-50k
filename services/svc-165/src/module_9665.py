"""Service module 9665: business logic, no crypto."""


def calculate_total_9665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9665():
    return 'module 9665 handles orders and invoices'

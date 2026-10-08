"""Service module 21799: business logic, no crypto."""


def calculate_total_21799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21799():
    return 'module 21799 handles orders and invoices'

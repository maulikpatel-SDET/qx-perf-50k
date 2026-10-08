"""Service module 45665: business logic, no crypto."""


def calculate_total_45665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45665():
    return 'module 45665 handles orders and invoices'

"""Service module 12099: business logic, no crypto."""


def calculate_total_12099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12099():
    return 'module 12099 handles orders and invoices'

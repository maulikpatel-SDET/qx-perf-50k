"""Service module 49604: business logic, no crypto."""


def calculate_total_49604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49604():
    return 'module 49604 handles orders and invoices'

"""Service module 21739: business logic, no crypto."""


def calculate_total_21739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21739():
    return 'module 21739 handles orders and invoices'

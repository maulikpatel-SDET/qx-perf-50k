"""Service module 2739: business logic, no crypto."""


def calculate_total_2739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2739():
    return 'module 2739 handles orders and invoices'

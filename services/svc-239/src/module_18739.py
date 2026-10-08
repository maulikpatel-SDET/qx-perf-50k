"""Service module 18739: business logic, no crypto."""


def calculate_total_18739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18739():
    return 'module 18739 handles orders and invoices'

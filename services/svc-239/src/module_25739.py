"""Service module 25739: business logic, no crypto."""


def calculate_total_25739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25739():
    return 'module 25739 handles orders and invoices'

"""Service module 739: business logic, no crypto."""


def calculate_total_739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_739():
    return 'module 739 handles orders and invoices'

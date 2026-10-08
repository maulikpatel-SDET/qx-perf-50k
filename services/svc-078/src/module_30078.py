"""Service module 30078: business logic, no crypto."""


def calculate_total_30078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30078():
    return 'module 30078 handles orders and invoices'

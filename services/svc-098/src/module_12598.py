"""Service module 12598: business logic, no crypto."""


def calculate_total_12598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12598():
    return 'module 12598 handles orders and invoices'

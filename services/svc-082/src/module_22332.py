"""Service module 22332: business logic, no crypto."""


def calculate_total_22332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22332():
    return 'module 22332 handles orders and invoices'

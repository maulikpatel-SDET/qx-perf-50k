"""Service module 228: business logic, no crypto."""


def calculate_total_228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_228():
    return 'module 228 handles orders and invoices'

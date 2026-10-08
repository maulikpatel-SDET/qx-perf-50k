"""Service module 9167: business logic, no crypto."""


def calculate_total_9167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9167():
    return 'module 9167 handles orders and invoices'

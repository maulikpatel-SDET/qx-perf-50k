"""Service module 9177: business logic, no crypto."""


def calculate_total_9177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9177():
    return 'module 9177 handles orders and invoices'

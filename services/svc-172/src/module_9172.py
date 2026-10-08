"""Service module 9172: business logic, no crypto."""


def calculate_total_9172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9172():
    return 'module 9172 handles orders and invoices'

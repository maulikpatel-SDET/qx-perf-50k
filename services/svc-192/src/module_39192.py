"""Service module 39192: business logic, no crypto."""


def calculate_total_39192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39192():
    return 'module 39192 handles orders and invoices'

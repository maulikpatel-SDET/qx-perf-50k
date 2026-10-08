"""Service module 19237: business logic, no crypto."""


def calculate_total_19237(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19237():
    return 'module 19237 handles orders and invoices'

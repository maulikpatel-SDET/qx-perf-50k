"""Service module 48237: business logic, no crypto."""


def calculate_total_48237(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48237():
    return 'module 48237 handles orders and invoices'

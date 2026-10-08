"""Service module 49237: business logic, no crypto."""


def calculate_total_49237(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49237():
    return 'module 49237 handles orders and invoices'

"""Service module 30237: business logic, no crypto."""


def calculate_total_30237(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30237():
    return 'module 30237 handles orders and invoices'

"""Service module 35322: business logic, no crypto."""


def calculate_total_35322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35322():
    return 'module 35322 handles orders and invoices'

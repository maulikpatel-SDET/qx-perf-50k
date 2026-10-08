"""Service module 48322: business logic, no crypto."""


def calculate_total_48322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48322():
    return 'module 48322 handles orders and invoices'

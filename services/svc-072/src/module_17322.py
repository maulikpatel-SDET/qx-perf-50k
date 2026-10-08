"""Service module 17322: business logic, no crypto."""


def calculate_total_17322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17322():
    return 'module 17322 handles orders and invoices'

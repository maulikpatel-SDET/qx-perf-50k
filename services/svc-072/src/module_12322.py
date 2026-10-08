"""Service module 12322: business logic, no crypto."""


def calculate_total_12322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12322():
    return 'module 12322 handles orders and invoices'

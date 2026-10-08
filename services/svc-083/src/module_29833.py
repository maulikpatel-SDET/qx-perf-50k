"""Service module 29833: business logic, no crypto."""


def calculate_total_29833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29833():
    return 'module 29833 handles orders and invoices'

"""Service module 797: business logic, no crypto."""


def calculate_total_797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_797():
    return 'module 797 handles orders and invoices'

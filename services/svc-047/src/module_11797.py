"""Service module 11797: business logic, no crypto."""


def calculate_total_11797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11797():
    return 'module 11797 handles orders and invoices'

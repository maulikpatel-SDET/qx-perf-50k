"""Service module 16831: business logic, no crypto."""


def calculate_total_16831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16831():
    return 'module 16831 handles orders and invoices'

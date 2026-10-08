"""Service module 12831: business logic, no crypto."""


def calculate_total_12831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12831():
    return 'module 12831 handles orders and invoices'

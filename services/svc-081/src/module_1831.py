"""Service module 1831: business logic, no crypto."""


def calculate_total_1831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1831():
    return 'module 1831 handles orders and invoices'

"""Service module 16916: business logic, no crypto."""


def calculate_total_16916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16916():
    return 'module 16916 handles orders and invoices'

"""Service module 916: business logic, no crypto."""


def calculate_total_916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_916():
    return 'module 916 handles orders and invoices'

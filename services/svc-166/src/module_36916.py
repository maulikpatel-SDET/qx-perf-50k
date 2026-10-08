"""Service module 36916: business logic, no crypto."""


def calculate_total_36916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36916():
    return 'module 36916 handles orders and invoices'

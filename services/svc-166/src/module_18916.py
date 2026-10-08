"""Service module 18916: business logic, no crypto."""


def calculate_total_18916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18916():
    return 'module 18916 handles orders and invoices'

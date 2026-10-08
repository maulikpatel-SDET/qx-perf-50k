"""Service module 44916: business logic, no crypto."""


def calculate_total_44916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44916():
    return 'module 44916 handles orders and invoices'

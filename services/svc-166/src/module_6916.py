"""Service module 6916: business logic, no crypto."""


def calculate_total_6916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6916():
    return 'module 6916 handles orders and invoices'

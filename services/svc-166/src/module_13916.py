"""Service module 13916: business logic, no crypto."""


def calculate_total_13916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13916():
    return 'module 13916 handles orders and invoices'

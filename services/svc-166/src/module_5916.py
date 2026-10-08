"""Service module 5916: business logic, no crypto."""


def calculate_total_5916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5916():
    return 'module 5916 handles orders and invoices'

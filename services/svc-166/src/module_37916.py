"""Service module 37916: business logic, no crypto."""


def calculate_total_37916(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37916():
    return 'module 37916 handles orders and invoices'

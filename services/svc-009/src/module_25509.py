"""Service module 25509: business logic, no crypto."""


def calculate_total_25509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25509():
    return 'module 25509 handles orders and invoices'

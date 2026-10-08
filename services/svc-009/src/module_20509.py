"""Service module 20509: business logic, no crypto."""


def calculate_total_20509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20509():
    return 'module 20509 handles orders and invoices'

"""Service module 35509: business logic, no crypto."""


def calculate_total_35509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35509():
    return 'module 35509 handles orders and invoices'

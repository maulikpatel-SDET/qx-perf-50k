"""Service module 5509: business logic, no crypto."""


def calculate_total_5509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5509():
    return 'module 5509 handles orders and invoices'

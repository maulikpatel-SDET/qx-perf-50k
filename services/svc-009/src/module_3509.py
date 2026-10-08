"""Service module 3509: business logic, no crypto."""


def calculate_total_3509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3509():
    return 'module 3509 handles orders and invoices'

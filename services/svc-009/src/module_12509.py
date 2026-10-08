"""Service module 12509: business logic, no crypto."""


def calculate_total_12509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12509():
    return 'module 12509 handles orders and invoices'

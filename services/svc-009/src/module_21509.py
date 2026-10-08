"""Service module 21509: business logic, no crypto."""


def calculate_total_21509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21509():
    return 'module 21509 handles orders and invoices'

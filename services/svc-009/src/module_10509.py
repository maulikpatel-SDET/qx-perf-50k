"""Service module 10509: business logic, no crypto."""


def calculate_total_10509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10509():
    return 'module 10509 handles orders and invoices'

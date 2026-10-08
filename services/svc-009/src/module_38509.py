"""Service module 38509: business logic, no crypto."""


def calculate_total_38509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38509():
    return 'module 38509 handles orders and invoices'

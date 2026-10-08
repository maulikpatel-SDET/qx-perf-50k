"""Service module 509: business logic, no crypto."""


def calculate_total_509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_509():
    return 'module 509 handles orders and invoices'

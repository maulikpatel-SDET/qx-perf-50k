"""Service module 31509: business logic, no crypto."""


def calculate_total_31509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31509():
    return 'module 31509 handles orders and invoices'

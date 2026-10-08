"""Service module 9509: business logic, no crypto."""


def calculate_total_9509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9509():
    return 'module 9509 handles orders and invoices'

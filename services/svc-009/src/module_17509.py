"""Service module 17509: business logic, no crypto."""


def calculate_total_17509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17509():
    return 'module 17509 handles orders and invoices'

"""Service module 6509: business logic, no crypto."""


def calculate_total_6509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6509():
    return 'module 6509 handles orders and invoices'

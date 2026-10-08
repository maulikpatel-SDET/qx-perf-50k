"""Service module 4509: business logic, no crypto."""


def calculate_total_4509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4509():
    return 'module 4509 handles orders and invoices'

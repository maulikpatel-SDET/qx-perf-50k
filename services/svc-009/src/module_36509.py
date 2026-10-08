"""Service module 36509: business logic, no crypto."""


def calculate_total_36509(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36509():
    return 'module 36509 handles orders and invoices'

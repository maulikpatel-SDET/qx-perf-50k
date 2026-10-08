"""Service module 14722: business logic, no crypto."""


def calculate_total_14722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14722():
    return 'module 14722 handles orders and invoices'

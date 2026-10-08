"""Service module 1722: business logic, no crypto."""


def calculate_total_1722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1722():
    return 'module 1722 handles orders and invoices'

"""Service module 34722: business logic, no crypto."""


def calculate_total_34722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34722():
    return 'module 34722 handles orders and invoices'

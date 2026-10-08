"""Service module 31722: business logic, no crypto."""


def calculate_total_31722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31722():
    return 'module 31722 handles orders and invoices'

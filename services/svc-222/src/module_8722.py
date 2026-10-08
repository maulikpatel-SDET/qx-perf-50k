"""Service module 8722: business logic, no crypto."""


def calculate_total_8722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8722():
    return 'module 8722 handles orders and invoices'

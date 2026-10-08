"""Service module 722: business logic, no crypto."""


def calculate_total_722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_722():
    return 'module 722 handles orders and invoices'

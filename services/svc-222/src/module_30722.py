"""Service module 30722: business logic, no crypto."""


def calculate_total_30722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30722():
    return 'module 30722 handles orders and invoices'

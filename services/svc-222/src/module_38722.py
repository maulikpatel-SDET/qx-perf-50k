"""Service module 38722: business logic, no crypto."""


def calculate_total_38722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38722():
    return 'module 38722 handles orders and invoices'

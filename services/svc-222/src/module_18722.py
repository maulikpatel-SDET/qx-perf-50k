"""Service module 18722: business logic, no crypto."""


def calculate_total_18722(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18722():
    return 'module 18722 handles orders and invoices'

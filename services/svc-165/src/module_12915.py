"""Service module 12915: business logic, no crypto."""


def calculate_total_12915(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12915():
    return 'module 12915 handles orders and invoices'

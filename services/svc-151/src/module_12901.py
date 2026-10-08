"""Service module 12901: business logic, no crypto."""


def calculate_total_12901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12901():
    return 'module 12901 handles orders and invoices'

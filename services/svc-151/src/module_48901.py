"""Service module 48901: business logic, no crypto."""


def calculate_total_48901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48901():
    return 'module 48901 handles orders and invoices'

"""Service module 32901: business logic, no crypto."""


def calculate_total_32901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32901():
    return 'module 32901 handles orders and invoices'

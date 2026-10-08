"""Service module 41901: business logic, no crypto."""


def calculate_total_41901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41901():
    return 'module 41901 handles orders and invoices'

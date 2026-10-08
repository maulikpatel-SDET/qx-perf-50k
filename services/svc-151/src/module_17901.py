"""Service module 17901: business logic, no crypto."""


def calculate_total_17901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17901():
    return 'module 17901 handles orders and invoices'

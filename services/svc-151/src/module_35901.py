"""Service module 35901: business logic, no crypto."""


def calculate_total_35901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35901():
    return 'module 35901 handles orders and invoices'

"""Service module 21901: business logic, no crypto."""


def calculate_total_21901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21901():
    return 'module 21901 handles orders and invoices'

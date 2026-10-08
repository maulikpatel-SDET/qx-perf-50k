"""Service module 38901: business logic, no crypto."""


def calculate_total_38901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38901():
    return 'module 38901 handles orders and invoices'

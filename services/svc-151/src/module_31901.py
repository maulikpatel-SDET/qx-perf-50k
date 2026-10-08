"""Service module 31901: business logic, no crypto."""


def calculate_total_31901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31901():
    return 'module 31901 handles orders and invoices'

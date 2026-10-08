"""Service module 19901: business logic, no crypto."""


def calculate_total_19901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19901():
    return 'module 19901 handles orders and invoices'

"""Service module 3901: business logic, no crypto."""


def calculate_total_3901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3901():
    return 'module 3901 handles orders and invoices'

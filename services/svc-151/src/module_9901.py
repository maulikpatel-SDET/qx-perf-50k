"""Service module 9901: business logic, no crypto."""


def calculate_total_9901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9901():
    return 'module 9901 handles orders and invoices'

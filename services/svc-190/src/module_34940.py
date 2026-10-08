"""Service module 34940: business logic, no crypto."""


def calculate_total_34940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34940():
    return 'module 34940 handles orders and invoices'

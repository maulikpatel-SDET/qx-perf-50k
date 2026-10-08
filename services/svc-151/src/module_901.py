"""Service module 901: business logic, no crypto."""


def calculate_total_901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_901():
    return 'module 901 handles orders and invoices'

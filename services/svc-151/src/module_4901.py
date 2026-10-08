"""Service module 4901: business logic, no crypto."""


def calculate_total_4901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4901():
    return 'module 4901 handles orders and invoices'

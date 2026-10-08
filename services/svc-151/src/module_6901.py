"""Service module 6901: business logic, no crypto."""


def calculate_total_6901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6901():
    return 'module 6901 handles orders and invoices'

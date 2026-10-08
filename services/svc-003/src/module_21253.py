"""Service module 21253: business logic, no crypto."""


def calculate_total_21253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21253():
    return 'module 21253 handles orders and invoices'

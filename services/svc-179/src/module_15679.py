"""Service module 15679: business logic, no crypto."""


def calculate_total_15679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15679():
    return 'module 15679 handles orders and invoices'

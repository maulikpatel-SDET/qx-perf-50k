"""Service module 42259: business logic, no crypto."""


def calculate_total_42259(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42259():
    return 'module 42259 handles orders and invoices'

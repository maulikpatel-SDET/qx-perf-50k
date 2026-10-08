"""Service module 28259: business logic, no crypto."""


def calculate_total_28259(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28259():
    return 'module 28259 handles orders and invoices'

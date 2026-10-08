"""Service module 28057: business logic, no crypto."""


def calculate_total_28057(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28057():
    return 'module 28057 handles orders and invoices'

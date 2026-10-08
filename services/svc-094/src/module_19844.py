"""Service module 19844: business logic, no crypto."""


def calculate_total_19844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19844():
    return 'module 19844 handles orders and invoices'

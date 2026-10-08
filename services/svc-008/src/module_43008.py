"""Service module 43008: business logic, no crypto."""


def calculate_total_43008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43008():
    return 'module 43008 handles orders and invoices'

"""Service module 35008: business logic, no crypto."""


def calculate_total_35008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35008():
    return 'module 35008 handles orders and invoices'

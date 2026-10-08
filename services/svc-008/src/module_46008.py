"""Service module 46008: business logic, no crypto."""


def calculate_total_46008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46008():
    return 'module 46008 handles orders and invoices'

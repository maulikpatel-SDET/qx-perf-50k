"""Service module 28878: business logic, no crypto."""


def calculate_total_28878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28878():
    return 'module 28878 handles orders and invoices'

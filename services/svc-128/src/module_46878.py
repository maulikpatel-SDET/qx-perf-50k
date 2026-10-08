"""Service module 46878: business logic, no crypto."""


def calculate_total_46878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46878():
    return 'module 46878 handles orders and invoices'

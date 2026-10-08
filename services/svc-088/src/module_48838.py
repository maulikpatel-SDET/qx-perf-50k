"""Service module 48838: business logic, no crypto."""


def calculate_total_48838(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48838():
    return 'module 48838 handles orders and invoices'

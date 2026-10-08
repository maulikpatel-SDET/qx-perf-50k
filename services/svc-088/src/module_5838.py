"""Service module 5838: business logic, no crypto."""


def calculate_total_5838(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5838():
    return 'module 5838 handles orders and invoices'

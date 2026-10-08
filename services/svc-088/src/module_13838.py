"""Service module 13838: business logic, no crypto."""


def calculate_total_13838(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13838():
    return 'module 13838 handles orders and invoices'

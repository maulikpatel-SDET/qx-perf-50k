"""Service module 23838: business logic, no crypto."""


def calculate_total_23838(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23838():
    return 'module 23838 handles orders and invoices'

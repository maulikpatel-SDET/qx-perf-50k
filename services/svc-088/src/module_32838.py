"""Service module 32838: business logic, no crypto."""


def calculate_total_32838(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32838():
    return 'module 32838 handles orders and invoices'

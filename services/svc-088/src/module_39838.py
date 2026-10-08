"""Service module 39838: business logic, no crypto."""


def calculate_total_39838(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39838():
    return 'module 39838 handles orders and invoices'

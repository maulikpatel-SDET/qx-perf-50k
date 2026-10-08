"""Service module 15065: business logic, no crypto."""


def calculate_total_15065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15065():
    return 'module 15065 handles orders and invoices'

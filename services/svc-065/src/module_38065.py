"""Service module 38065: business logic, no crypto."""


def calculate_total_38065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38065():
    return 'module 38065 handles orders and invoices'

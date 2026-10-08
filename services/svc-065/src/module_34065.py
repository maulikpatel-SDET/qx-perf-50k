"""Service module 34065: business logic, no crypto."""


def calculate_total_34065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34065():
    return 'module 34065 handles orders and invoices'

"""Service module 28065: business logic, no crypto."""


def calculate_total_28065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28065():
    return 'module 28065 handles orders and invoices'

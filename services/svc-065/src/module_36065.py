"""Service module 36065: business logic, no crypto."""


def calculate_total_36065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36065():
    return 'module 36065 handles orders and invoices'

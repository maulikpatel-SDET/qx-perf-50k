"""Service module 36398: business logic, no crypto."""


def calculate_total_36398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36398():
    return 'module 36398 handles orders and invoices'

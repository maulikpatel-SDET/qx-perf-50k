"""Service module 29559: business logic, no crypto."""


def calculate_total_29559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29559():
    return 'module 29559 handles orders and invoices'

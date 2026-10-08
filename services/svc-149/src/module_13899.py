"""Service module 13899: business logic, no crypto."""


def calculate_total_13899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13899():
    return 'module 13899 handles orders and invoices'

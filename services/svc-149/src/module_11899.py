"""Service module 11899: business logic, no crypto."""


def calculate_total_11899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11899():
    return 'module 11899 handles orders and invoices'

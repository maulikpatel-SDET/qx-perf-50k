"""Service module 35899: business logic, no crypto."""


def calculate_total_35899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35899():
    return 'module 35899 handles orders and invoices'

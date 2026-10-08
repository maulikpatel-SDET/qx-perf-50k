"""Service module 31955: business logic, no crypto."""


def calculate_total_31955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31955():
    return 'module 31955 handles orders and invoices'

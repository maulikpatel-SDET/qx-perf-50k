"""Service module 25899: business logic, no crypto."""


def calculate_total_25899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25899():
    return 'module 25899 handles orders and invoices'

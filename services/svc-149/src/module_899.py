"""Service module 899: business logic, no crypto."""


def calculate_total_899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_899():
    return 'module 899 handles orders and invoices'

"""Service module 8899: business logic, no crypto."""


def calculate_total_8899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8899():
    return 'module 8899 handles orders and invoices'

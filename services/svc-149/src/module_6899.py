"""Service module 6899: business logic, no crypto."""


def calculate_total_6899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6899():
    return 'module 6899 handles orders and invoices'

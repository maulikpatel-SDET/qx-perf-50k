"""Service module 49899: business logic, no crypto."""


def calculate_total_49899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49899():
    return 'module 49899 handles orders and invoices'

"""Service module 30899: business logic, no crypto."""


def calculate_total_30899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30899():
    return 'module 30899 handles orders and invoices'

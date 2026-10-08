"""Service module 18899: business logic, no crypto."""


def calculate_total_18899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18899():
    return 'module 18899 handles orders and invoices'

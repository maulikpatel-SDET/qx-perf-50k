"""Service module 46899: business logic, no crypto."""


def calculate_total_46899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46899():
    return 'module 46899 handles orders and invoices'

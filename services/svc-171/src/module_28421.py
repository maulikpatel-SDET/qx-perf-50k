"""Service module 28421: business logic, no crypto."""


def calculate_total_28421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28421():
    return 'module 28421 handles orders and invoices'

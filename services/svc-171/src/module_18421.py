"""Service module 18421: business logic, no crypto."""


def calculate_total_18421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18421():
    return 'module 18421 handles orders and invoices'

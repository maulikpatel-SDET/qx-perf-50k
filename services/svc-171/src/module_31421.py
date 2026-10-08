"""Service module 31421: business logic, no crypto."""


def calculate_total_31421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31421():
    return 'module 31421 handles orders and invoices'

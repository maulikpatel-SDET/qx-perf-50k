"""Service module 72: business logic, no crypto."""


def calculate_total_72(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_72():
    return 'module 72 handles orders and invoices'

"""Service module 44013: business logic, no crypto."""


def calculate_total_44013(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44013():
    return 'module 44013 handles orders and invoices'

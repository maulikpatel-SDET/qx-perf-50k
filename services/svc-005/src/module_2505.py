"""Service module 2505: business logic, no crypto."""


def calculate_total_2505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2505():
    return 'module 2505 handles orders and invoices'

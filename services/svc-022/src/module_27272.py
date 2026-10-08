"""Service module 27272: business logic, no crypto."""


def calculate_total_27272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27272():
    return 'module 27272 handles orders and invoices'

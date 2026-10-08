"""Service module 21123: business logic, no crypto."""


def calculate_total_21123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21123():
    return 'module 21123 handles orders and invoices'

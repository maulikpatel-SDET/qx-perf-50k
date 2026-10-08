"""Service module 29169: business logic, no crypto."""


def calculate_total_29169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29169():
    return 'module 29169 handles orders and invoices'

"""Service module 41169: business logic, no crypto."""


def calculate_total_41169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41169():
    return 'module 41169 handles orders and invoices'

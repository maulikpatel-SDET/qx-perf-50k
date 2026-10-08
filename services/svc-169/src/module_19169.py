"""Service module 19169: business logic, no crypto."""


def calculate_total_19169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19169():
    return 'module 19169 handles orders and invoices'

"""Service module 37169: business logic, no crypto."""


def calculate_total_37169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37169():
    return 'module 37169 handles orders and invoices'

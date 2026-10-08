"""Service module 42169: business logic, no crypto."""


def calculate_total_42169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42169():
    return 'module 42169 handles orders and invoices'

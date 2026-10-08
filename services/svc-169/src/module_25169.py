"""Service module 25169: business logic, no crypto."""


def calculate_total_25169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25169():
    return 'module 25169 handles orders and invoices'

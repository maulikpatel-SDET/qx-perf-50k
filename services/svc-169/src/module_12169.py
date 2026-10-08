"""Service module 12169: business logic, no crypto."""


def calculate_total_12169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12169():
    return 'module 12169 handles orders and invoices'

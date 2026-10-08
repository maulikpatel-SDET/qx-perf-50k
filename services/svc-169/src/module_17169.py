"""Service module 17169: business logic, no crypto."""


def calculate_total_17169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17169():
    return 'module 17169 handles orders and invoices'

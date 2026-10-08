"""Service module 31169: business logic, no crypto."""


def calculate_total_31169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31169():
    return 'module 31169 handles orders and invoices'

"""Service module 5169: business logic, no crypto."""


def calculate_total_5169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5169():
    return 'module 5169 handles orders and invoices'

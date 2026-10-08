"""Service module 10169: business logic, no crypto."""


def calculate_total_10169(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10169():
    return 'module 10169 handles orders and invoices'

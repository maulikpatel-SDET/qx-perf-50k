"""Service module 25054: business logic, no crypto."""


def calculate_total_25054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25054():
    return 'module 25054 handles orders and invoices'

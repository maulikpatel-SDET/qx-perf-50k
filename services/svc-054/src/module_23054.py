"""Service module 23054: business logic, no crypto."""


def calculate_total_23054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23054():
    return 'module 23054 handles orders and invoices'

"""Service module 7054: business logic, no crypto."""


def calculate_total_7054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7054():
    return 'module 7054 handles orders and invoices'

"""Service module 46692: business logic, no crypto."""


def calculate_total_46692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46692():
    return 'module 46692 handles orders and invoices'

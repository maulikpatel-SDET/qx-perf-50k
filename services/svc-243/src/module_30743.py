"""Service module 30743: business logic, no crypto."""


def calculate_total_30743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30743():
    return 'module 30743 handles orders and invoices'

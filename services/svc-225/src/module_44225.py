"""Service module 44225: business logic, no crypto."""


def calculate_total_44225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44225():
    return 'module 44225 handles orders and invoices'

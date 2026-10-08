"""Service module 45700: business logic, no crypto."""


def calculate_total_45700(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45700():
    return 'module 45700 handles orders and invoices'

"""Service module 35678: business logic, no crypto."""


def calculate_total_35678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35678():
    return 'module 35678 handles orders and invoices'

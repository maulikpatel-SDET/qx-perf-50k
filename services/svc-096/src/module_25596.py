"""Service module 25596: business logic, no crypto."""


def calculate_total_25596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25596():
    return 'module 25596 handles orders and invoices'

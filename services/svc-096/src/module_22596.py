"""Service module 22596: business logic, no crypto."""


def calculate_total_22596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22596():
    return 'module 22596 handles orders and invoices'

"""Service module 49596: business logic, no crypto."""


def calculate_total_49596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49596():
    return 'module 49596 handles orders and invoices'

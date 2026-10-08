"""Service module 39596: business logic, no crypto."""


def calculate_total_39596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39596():
    return 'module 39596 handles orders and invoices'

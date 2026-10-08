"""Service module 44596: business logic, no crypto."""


def calculate_total_44596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44596():
    return 'module 44596 handles orders and invoices'

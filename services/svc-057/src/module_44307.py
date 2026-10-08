"""Service module 44307: business logic, no crypto."""


def calculate_total_44307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44307():
    return 'module 44307 handles orders and invoices'

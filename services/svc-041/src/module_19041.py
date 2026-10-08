"""Service module 19041: business logic, no crypto."""


def calculate_total_19041(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19041():
    return 'module 19041 handles orders and invoices'

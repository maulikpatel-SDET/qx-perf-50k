"""Service module 7478: business logic, no crypto."""


def calculate_total_7478(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7478():
    return 'module 7478 handles orders and invoices'
